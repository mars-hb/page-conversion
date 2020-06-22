#!/usr/bin/env python3

import math

PAGE_SIZE = 0x1000

PAGE_TABLE = {
    0x00000: 0x96,
    0x00001: 0x4000000,
    0x00400: 0x220A,
    0x00401: 0x31,
    0x01000: 0x5DE7,
    0x01001: 0x2F01,
    0x10002: 0x4004,
    0x1000E: 0x3345E,
    0x1000F: 0xC0C12,
    0x10010: 0x01DE4,
    0x10011: 0x51A3B,
    0x7FFFC: 0x2000,
    0x7FFFD: 0x2001,
    0x7FFFE: 0x2002,
    0x7FFFF: 0xAB170,
    0x80000: 0x123DE9
}


inpt = input("Bitte geben Sie eine virtuelle Adresse ein: ")

virt_addr = int(inpt, 16)

page = math.floor(virt_addr / PAGE_SIZE) # Schritt 1 (Teilen der virtuellen Adresse durch die Page Size)

if page not in PAGE_TABLE:
    raise ValueError(f"Page {page} nicht in Page Tabelle vorhanden")

page_frame = PAGE_TABLE[page] # Schritt 2 (Abbildung Page -> Page-Frame bzw. Nachschauen in Page Tabelle)

page_address = (page_frame * PAGE_SIZE) << 12 # 12 bit Offset, weil Page Size = 2^12

offset = virt_addr % PAGE_SIZE

real_address = page_address + offset # Schritt 3 (Offset bzw. Divisionsrest hinzuaddieren)


print(30 * "-" + "\nErgebnis:")
print(f"Virtuelle Adresse: {hex(virt_addr)}")
print(f"Page: {hex(page)}")
print(f"Page Frame: {hex(page_frame)}")
print(f"Page Adresse: {hex(page_address)}")
print(f"Offset: {hex(offset)}")
print(f"Reale Adresse: {hex(real_address)}")
print(30 * "-")