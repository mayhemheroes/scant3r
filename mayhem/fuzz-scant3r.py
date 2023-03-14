#! /usr/bin/python3

import atheris
import sys
import io

with atheris.instrument_imports():
    from scant3r.core.utils import extract_headers, urlencoder

def TestOneInput(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    data = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    extract_headers(data)
    urlencoder(data, len(data))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
