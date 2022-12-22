VERSION = "0.1.0"


def validate_asn(asn: int):
    if asn < 0:
        raise ValueError("ASN can not be negative.")
