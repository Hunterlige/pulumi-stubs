

import builtins as _builtins
import pulumi
from enum import Enum

__all__ = ['ChannelBinding', 'ExternalAccess', 'FilteredSync', 'KerberosArmoring', 'KerberosRc4Encryption', 'LdapSigning', 'Ldaps', 'NotifyDcAdmins', 'NotifyGlobalAdmins', 'NtlmV1', 'Status', 'SyncKerberosPasswords', 'SyncNtlmPasswords', 'SyncOnPremPasswords', 'SyncScope', 'TlsV1']
@pulumi.type_token("azure-native:aad:ChannelBinding")
class ChannelBinding(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:ExternalAccess")
class ExternalAccess(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:FilteredSync")
class FilteredSync(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:KerberosArmoring")
class KerberosArmoring(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:KerberosRc4Encryption")
class KerberosRc4Encryption(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:LdapSigning")
class LdapSigning(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:Ldaps")
class Ldaps(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:NotifyDcAdmins")
class NotifyDcAdmins(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:NotifyGlobalAdmins")
class NotifyGlobalAdmins(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:NtlmV1")
class NtlmV1(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:Status")
class Status(_builtins.str, Enum):
    
    NONE = ...
    RUNNING = ...
    OK = ...
    FAILURE = ...
    WARNING = ...
    SKIPPED = ...


@pulumi.type_token("azure-native:aad:SyncKerberosPasswords")
class SyncKerberosPasswords(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:SyncNtlmPasswords")
class SyncNtlmPasswords(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:SyncOnPremPasswords")
class SyncOnPremPasswords(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


@pulumi.type_token("azure-native:aad:SyncScope")
class SyncScope(_builtins.str, Enum):
    
    ALL = ...
    CLOUD_ONLY = ...


@pulumi.type_token("azure-native:aad:TlsV1")
class TlsV1(_builtins.str, Enum):
    
    ENABLED = ...
    DISABLED = ...


