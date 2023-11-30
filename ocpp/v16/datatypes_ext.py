from dataclasses import dataclass
from typing import Optional, List
from ocpp.v16.enums import (
    InstallCertificateUseEnumType,
    HashAlgorithmEnumType
)


@dataclass
class InstallCertificateReq:
    certificateType: InstallCertificateUseEnumType
    # Mock Certificate
    cert = """
-----BEGIN CERTIFICATE-----
MIICUzCCAfmgAwIBAgIQaasA0lm730LOgFKa0wzl7TAKBggqhkjOPQQDAjBVMQsw
CQYDVQQGEwJERTEVMBMGA1UEChMMSHViamVjdCBHbWJIMRMwEQYKCZImiZPyLGQB
GRYDVjJHMRowGAYDVQQDExFWMkcgUm9vdCBDQSBRQSBHMTAgFw0xOTA0MjYwODM3
MTVaGA8yMDU5MDQyNjA4MzcxNVowVTELMAkGA1UEBhMCREUxFTATBgNVBAoTDEh1
YmplY3QgR21iSDETMBEGCgmSJomT8ixkARkWA1YyRzEaMBgGA1UEAxMRVjJHIFJv
b3QgQ0EgUUEgRzEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAShT8kSNcC+74TN
D82On2Y2TOf8mYfxw73lKZ7t9cmEXHpMdAgsWBQ4LI+pOMhe6NOHzJbzP38kQTg4
zLfw3kU0o4GoMIGlMBMGA1UdJQQMMAoGCCsGAQUFBwMJMA8GA1UdEwEB/wQFMAMB
Af8wEQYDVR0OBAoECEtF/4Il/BCWMEUGA1UdIAQ+MDwwOgYMKwYBBAGCxDUBAgEA
MCowKAYIKwYBBQUHAgEWHGh0dHBzOi8vd3d3Lmh1YmplY3QuY29tL3BraS8wEwYD
VR0jBAwwCoAIS0X/giX8EJYwDgYDVR0PAQH/BAQDAgEGMAoGCCqGSM49BAMCA0gA
MEUCIQCq3Qx2BLYVFb7Lt5XXpSlUViYv4cIUOQE1Ce9o2Jyy1QIgZRmVzMVjHZA+
toiM000PCUrLppqbLpcRN4MP8kE0OhU=
-----END CERTIFICATE-----
"""
    certificate: str = cert


@dataclass
class GetInstallCertificateIdsReq:
    certificateType: Optional[List] = None



@dataclass
class CertificateHashDataType:
    hashAlgorithm: HashAlgorithmEnumType
    issuerNameHash: str
    issuerKeyHash: str
    serialNumber: str



@dataclass
class DeleteCertificateReq:
    certificateHashData: CertificateHashDataType
