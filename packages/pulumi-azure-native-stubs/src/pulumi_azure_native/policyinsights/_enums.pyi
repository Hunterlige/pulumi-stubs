

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ComplianceState', 'ResourceDiscoveryMode']
@pulumi.type_token("azure-native:policyinsights:ComplianceState")
class ComplianceState(_builtins.str, Enum):
    
    COMPLIANT = ...
    NON_COMPLIANT = ...
    UNKNOWN = ...


@pulumi.type_token("azure-native:policyinsights:ResourceDiscoveryMode")
class ResourceDiscoveryMode(_builtins.str, Enum):
    
    EXISTING_NON_COMPLIANT = ...
    RE_EVALUATE_COMPLIANCE = ...


