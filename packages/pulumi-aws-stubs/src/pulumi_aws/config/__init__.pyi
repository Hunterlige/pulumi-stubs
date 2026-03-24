import builtins as _builtins
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import (
    Any,
    Mapping,
    NotRequired,
    Optional,
    Sequence,
    TypeAlias,
    TypedDict,
    Union,
    overload,
)
from .. import _utilities
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
accessKey: Optional[str]
allowedAccountIds: Optional[str]
assumeRoleWithWebIdentity: Optional[str]
assumeRoles: Optional[str]
customCaBundle: Optional[str]
defaultTags: Optional[str]
ec2MetadataServiceEndpoint: Optional[str]
ec2MetadataServiceEndpointMode: Optional[str]
endpoints: Optional[str]
forbiddenAccountIds: Optional[str]
httpProxy: Optional[str]
httpsProxy: Optional[str]
ignoreTags: Optional[str]
insecure: Optional[bool]
maxRetries: Optional[int]
noProxy: Optional[str]
profile: Optional[str]
region: Optional[str]
retryMode: Optional[str]
s3UsEast1RegionalEndpoint: Optional[str]
s3UsePathStyle: Optional[bool]
secretKey: Optional[str]
sharedConfigFiles: Optional[str]
sharedCredentialsFiles: Optional[str]
skipCredentialsValidation: bool
skipMetadataApiCheck: Optional[bool]
skipRegionValidation: bool
skipRequestingAccountId: Optional[bool]
stsRegion: Optional[str]
tagPolicyCompliance: Optional[str]
token: Optional[str]
tokenBucketRateLimiterCapacity: Optional[int]
useDualstackEndpoint: Optional[bool]
useFipsEndpoint: Optional[bool]
userAgents: Optional[str]
