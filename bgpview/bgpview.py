from bgpview.api_client import APIClient
from bgpview.util import validate_asn
from ipaddress import ip_network


class BGPView(APIClient):
    def __init__(self, user_agent: str = None):
        super(BGPView, self).__init__(user_agent)

    def get_asn(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}")
        return ASN(j.get("data", {}), self)

    def get_asn_prefixes(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}/prefixes")
        return ASNPrefixes(j.get("data", {}), self)

    def get_asn_peers(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}/peers")
        return ASNPeers(j.get("data", {}), self)

    def get_asn_upstreams(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}/upstreams")
        return ASNUpstreams(j.get("data", {}), self)

    def get_asn_downstreams(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}/downstreams")
        return ASNDownstreams(j.get("data", {}), self)

    def get_asn_ixs(self, asn: int):
        asn = int(asn)
        validate_asn(asn)
        j = self.get(f"/asn/{asn}/ixs")
        return ASNIXs(j.get("data", {}), self)

    def get_prefix(self, prefix: str):
        prefix = ip_network(prefix)
        j = self.get(f"/prefix/{prefix.with_prefixlen}")
        return Prefix(j.get("data", {}), self)


class BGPViewResource:
    def __init__(self, data: dict, bgpview_client: BGPView):
        self.bgpview_client = bgpview_client
        for key in data:
            setattr(self, key, data[key])

class Prefix(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(Prefixe, self).__init__(data, bgpview_client)

class ASNPrefixes(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASNPrefixes, self).__init__(data, bgpview_client)


class ASNPeers(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASNPeers, self).__init__(data, bgpview_client)


class ASNUpstreams(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASNUpstreams, self).__init__(data, bgpview_client)


class ASNDownstreams(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASNDownstreams, self).__init__(data, bgpview_client)


class ASNIXs(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASNIXs, self).__init__(data, bgpview_client)


class ASN(BGPViewResource):
    def __init__(self, data: dict, bgpview_client: BGPView):
        super(ASN, self).__init__(data, bgpview_client)
        self.asn = None

    def get_prefixes(self) -> ASNPrefixes:
        return self.bgpview_client.get_asn_prefixes(self.asn)

    def get_peers(self) -> ASNPeers:
        return self.bgpview_client.get_asn_peers(self.asn)

    def get_upstreams(self) -> ASNUpstreams:
        return self.bgpview_client.get_asn_upstreams(self.asn)

    def get_downstreams(self) -> ASNDownstreams:
        return self.bgpview_client.get_asn_downstreams(self.asn)

    def get_ixs(self) -> ASNIXs:
        return self.bgpview_client.get_asn_ixs(self.asn)

