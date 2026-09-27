"""Odcisk SHA-256 certyfikatu, którym podpisano plik `.apk`.

Czyta blok podpisu APK (schemat v2 albo v3) — pliki z EAS przy minSdk 24
NIE MAJĄ podpisu v1 (`META-INF/*.RSA`), więc `keytool -printcert -jarfile`
nic w nich nie widzi. Skrypt nie sprawdza kryptograficznie podpisu (to robi
Android przy instalacji); jego zadanie to wskazać, CZYIM kluczem plik
podpisano, żeby przebieg `wydaj` odmówił wydania pliku z obcym kluczem.

Użycie: python3 sprawdz_podpis.py oplaca-sie.apk  → wypisuje odcisk (hex).
"""

import hashlib
import struct
import sys

V2, V3 = 0x7109871A, 0xF05368C0


def z_dlugoscia(b: bytes, o: int) -> tuple[bytes, int]:
    n = struct.unpack("<I", b[o : o + 4])[0]
    return b[o + 4 : o + 4 + n], o + 4 + n


def odcisk(sciezka: str) -> str:
    d = open(sciezka, "rb").read()
    eocd = d.rfind(b"PK\x05\x06")
    if eocd < 0:
        raise SystemExit("To nie jest plik ZIP/APK.")
    cd = struct.unpack("<I", d[eocd + 16 : eocd + 20])[0]
    if d[cd - 16 : cd] != b"APK Sig Block 42":
        raise SystemExit("Brak bloku podpisu APK (v2/v3).")
    rozmiar = struct.unpack("<Q", d[cd - 24 : cd - 16])[0]
    p = cd - rozmiar - 8 + 8
    znalezione = {}
    while p < cd - 24:
        n, ident = struct.unpack("<QI", d[p : p + 12])
        wartosc = d[p + 12 : p + 8 + n]
        p += 8 + n
        if ident in (V2, V3):
            podpisujacy, _ = z_dlugoscia(wartosc, 0)
            pierwszy, _ = z_dlugoscia(podpisujacy, 0)
            dane, _ = z_dlugoscia(pierwszy, 0)
            _, o = z_dlugoscia(dane, 0)  # skróty
            certyfikaty, _ = z_dlugoscia(dane, o)
            cert, _ = z_dlugoscia(certyfikaty, 0)
            znalezione[ident] = hashlib.sha256(cert).hexdigest()
    if not znalezione:
        raise SystemExit("Blok podpisu bez schematu v2/v3.")
    if len(set(znalezione.values())) != 1:
        raise SystemExit("v2 i v3 podają różne certyfikaty — przerywam.")
    return next(iter(znalezione.values()))


if __name__ == "__main__":
    print(odcisk(sys.argv[1]))
