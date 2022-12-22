from bgpview import BGPView
import pytest



def test_get_prefix():
    prefix = "68.100.0.0/16"
    expected_asn = 22773

    viewer = BGPView()
    p = viewer.get_prefix(prefix)
    assert p.prefix == prefix
    assert p.asns[0]['asn'] == expected_asn


