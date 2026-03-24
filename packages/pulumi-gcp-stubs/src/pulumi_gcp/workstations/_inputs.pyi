

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['WorkstationClusterConditionArgs', 'WorkstationClusterConditionArgsDict', 'WorkstationClusterDomainConfigArgs', 'WorkstationClusterDomainConfigArgsDict', 'WorkstationClusterPrivateClusterConfigArgs', 'WorkstationClusterPrivateClusterConfigArgsDict', 'WorkstationConfigAllowedPortArgs', 'WorkstationConfigAllowedPortArgsDict', 'WorkstationConfigConditionArgs', 'WorkstationConfigConditionArgsDict', 'WorkstationConfigContainerArgs', 'WorkstationConfigContainerArgsDict', 'WorkstationConfigEncryptionKeyArgs', 'WorkstationConfigEncryptionKeyArgsDict', 'WorkstationConfigEphemeralDirectoryArgs', 'WorkstationConfigEphemeralDirectoryArgsDict', 'WorkstationConfigEphemeralDirectoryGcePdArgs', 'WorkstationConfigEphemeralDirectoryGcePdArgsDict', 'WorkstationConfigHostArgs', 'WorkstationConfigHostArgsDict', 'WorkstationConfigHostGceInstanceArgs', 'WorkstationConfigHostGceInstanceArgsDict', 'WorkstationConfigHostGceInstanceAcceleratorArgs', ..., 'WorkstationConfigHostGceInstanceBoostConfigArgs', ..., ..., ..., ..., ..., ..., ..., 'WorkstationConfigIamBindingConditionArgs', 'WorkstationConfigIamBindingConditionArgsDict', 'WorkstationConfigIamMemberConditionArgs', 'WorkstationConfigIamMemberConditionArgsDict', 'WorkstationConfigPersistentDirectoryArgs', 'WorkstationConfigPersistentDirectoryArgsDict', 'WorkstationConfigPersistentDirectoryGcePdArgs', 'WorkstationConfigPersistentDirectoryGcePdArgsDict', 'WorkstationConfigReadinessCheckArgs', 'WorkstationConfigReadinessCheckArgsDict', 'WorkstationIamBindingConditionArgs', 'WorkstationIamBindingConditionArgsDict', 'WorkstationIamMemberConditionArgs', 'WorkstationIamMemberConditionArgsDict']
class WorkstationClusterConditionArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationClusterConditionArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., details: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationClusterDomainConfigArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkstationClusterDomainConfigArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkstationClusterPrivateClusterConfigArgsDict(TypedDict):
    enable_private_endpoint: pulumi.Input[_builtins.bool]
    allowed_projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    cluster_hostname: NotRequired[pulumi.Input[_builtins.str]]
    service_attachment_uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationClusterPrivateClusterConfigArgs:
    def __init__(__self__, *, enable_private_endpoint: pulumi.Input[_builtins.bool], allowed_projects: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., cluster_hostname: Optional[pulumi.Input[_builtins.str]] = ..., service_attachment_uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enablePrivateEndpoint")
    def enable_private_endpoint(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_private_endpoint.setter
    def enable_private_endpoint(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedProjects")
    def allowed_projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_projects.setter
    def allowed_projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clusterHostname")
    def cluster_hostname(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cluster_hostname.setter
    def cluster_hostname(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAttachmentUri")
    def service_attachment_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_attachment_uri.setter
    def service_attachment_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigAllowedPortArgsDict(TypedDict):
    first: NotRequired[pulumi.Input[_builtins.int]]
    last: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkstationConfigAllowedPortArgs:
    def __init__(__self__, *, first: Optional[pulumi.Input[_builtins.int]] = ..., last: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def first(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @first.setter
    def first(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def last(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @last.setter
    def last(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class WorkstationConfigConditionArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigConditionArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., details: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigContainerArgsDict(TypedDict):
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    env: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    image: NotRequired[pulumi.Input[_builtins.str]]
    run_as_user: NotRequired[pulumi.Input[_builtins.int]]
    working_dir: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigContainerArgs:
    def __init__(__self__, *, args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., env: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., image: Optional[pulumi.Input[_builtins.str]] = ..., run_as_user: Optional[pulumi.Input[_builtins.int]] = ..., working_dir: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @args.setter
    def args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def commands(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @commands.setter
    def commands(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def env(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @env.setter
    def env(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @image.setter
    def image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @run_as_user.setter
    def run_as_user(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigEncryptionKeyArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]
    kms_key_service_account: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkstationConfigEncryptionKeyArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str], kms_key_service_account: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKeyServiceAccount")
    def kms_key_service_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key_service_account.setter
    def kms_key_service_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkstationConfigEphemeralDirectoryArgsDict(TypedDict):
    gce_pd: NotRequired[pulumi.Input[WorkstationConfigEphemeralDirectoryGcePdArgsDict]]
    mount_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigEphemeralDirectoryArgs:
    def __init__(__self__, *, gce_pd: Optional[pulumi.Input[WorkstationConfigEphemeralDirectoryGcePdArgs]] = ..., mount_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcePd")
    def gce_pd(self) -> Optional[pulumi.Input[WorkstationConfigEphemeralDirectoryGcePdArgs]]:
        
        ...
    
    @gce_pd.setter
    def gce_pd(self, value: Optional[pulumi.Input[WorkstationConfigEphemeralDirectoryGcePdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigEphemeralDirectoryGcePdArgsDict(TypedDict):
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]
    source_image: NotRequired[pulumi.Input[_builtins.str]]
    source_snapshot: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigEphemeralDirectoryGcePdArgs:
    def __init__(__self__, *, disk_type: Optional[pulumi.Input[_builtins.str]] = ..., read_only: Optional[pulumi.Input[_builtins.bool]] = ..., source_image: Optional[pulumi.Input[_builtins.str]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceImage")
    def source_image(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_image.setter
    def source_image(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot.setter
    def source_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigHostArgsDict(TypedDict):
    gce_instance: NotRequired[pulumi.Input[WorkstationConfigHostGceInstanceArgsDict]]


@pulumi.input_type
class WorkstationConfigHostArgs:
    def __init__(__self__, *, gce_instance: Optional[pulumi.Input[WorkstationConfigHostGceInstanceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gceInstance")
    def gce_instance(self) -> Optional[pulumi.Input[WorkstationConfigHostGceInstanceArgs]]:
        
        ...
    
    @gce_instance.setter
    def gce_instance(self, value: Optional[pulumi.Input[WorkstationConfigHostGceInstanceArgs]]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceArgsDict(TypedDict):
    accelerators: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceAcceleratorArgsDict]]]]
    boost_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigArgsDict]]]]
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    confidential_instance_config: NotRequired[pulumi.Input[WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgsDict]]
    disable_public_ip_addresses: NotRequired[pulumi.Input[_builtins.bool]]
    disable_ssh: NotRequired[pulumi.Input[_builtins.bool]]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    pool_size: NotRequired[pulumi.Input[_builtins.int]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    service_account_scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    shielded_instance_config: NotRequired[pulumi.Input[WorkstationConfigHostGceInstanceShieldedInstanceConfigArgsDict]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    vm_tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class WorkstationConfigHostGceInstanceArgs:
    def __init__(__self__, *, accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceAcceleratorArgs]]]] = ..., boost_configs: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigArgs]]]] = ..., boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., confidential_instance_config: Optional[pulumi.Input[WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgs]] = ..., disable_public_ip_addresses: Optional[pulumi.Input[_builtins.bool]] = ..., disable_ssh: Optional[pulumi.Input[_builtins.bool]] = ..., enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., pool_size: Optional[pulumi.Input[_builtins.int]] = ..., service_account: Optional[pulumi.Input[_builtins.str]] = ..., service_account_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., shielded_instance_config: Optional[pulumi.Input[WorkstationConfigHostGceInstanceShieldedInstanceConfigArgs]] = ..., tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., vm_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostConfigs")
    def boost_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigArgs]]]]:
        
        ...
    
    @boost_configs.setter
    def boost_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidentialInstanceConfig")
    def confidential_instance_config(self) -> Optional[pulumi.Input[WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgs]]:
        
        ...
    
    @confidential_instance_config.setter
    def confidential_instance_config(self, value: Optional[pulumi.Input[WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disablePublicIpAddresses")
    def disable_public_ip_addresses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_public_ip_addresses.setter
    def disable_public_ip_addresses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableSsh")
    def disable_ssh(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_ssh.setter
    def disable_ssh(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolSize")
    def pool_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @pool_size.setter
    def pool_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountScopes")
    def service_account_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @service_account_scopes.setter
    def service_account_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shieldedInstanceConfig")
    def shielded_instance_config(self) -> Optional[pulumi.Input[WorkstationConfigHostGceInstanceShieldedInstanceConfigArgs]]:
        
        ...
    
    @shielded_instance_config.setter
    def shielded_instance_config(self, value: Optional[pulumi.Input[WorkstationConfigHostGceInstanceShieldedInstanceConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmTags")
    def vm_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @vm_tags.setter
    def vm_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceAcceleratorArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkstationConfigHostGceInstanceAcceleratorArgs:
    def __init__(__self__, *, count: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceBoostConfigArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    accelerators: NotRequired[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgsDict]]]]
    boot_disk_size_gb: NotRequired[pulumi.Input[_builtins.int]]
    enable_nested_virtualization: NotRequired[pulumi.Input[_builtins.bool]]
    machine_type: NotRequired[pulumi.Input[_builtins.str]]
    pool_size: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class WorkstationConfigHostGceInstanceBoostConfigArgs:
    def __init__(__self__, *, id: pulumi.Input[_builtins.str], accelerators: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgs]]]] = ..., boot_disk_size_gb: Optional[pulumi.Input[_builtins.int]] = ..., enable_nested_virtualization: Optional[pulumi.Input[_builtins.bool]] = ..., machine_type: Optional[pulumi.Input[_builtins.str]] = ..., pool_size: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accelerators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgs]]]]:
        
        ...
    
    @accelerators.setter
    def accelerators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bootDiskSizeGb")
    def boot_disk_size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @boot_disk_size_gb.setter
    def boot_disk_size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableNestedVirtualization")
    def enable_nested_virtualization(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_nested_virtualization.setter
    def enable_nested_virtualization(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @machine_type.setter
    def machine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="poolSize")
    def pool_size(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @pool_size.setter
    def pool_size(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgsDict(TypedDict):
    count: pulumi.Input[_builtins.int]
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class WorkstationConfigHostGceInstanceBoostConfigAcceleratorArgs:
    def __init__(__self__, *, count: pulumi.Input[_builtins.int], type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def count(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @count.setter
    def count(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgsDict(TypedDict):
    enable_confidential_compute: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class WorkstationConfigHostGceInstanceConfidentialInstanceConfigArgs:
    def __init__(__self__, *, enable_confidential_compute: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConfidentialCompute")
    def enable_confidential_compute(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_confidential_compute.setter
    def enable_confidential_compute(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WorkstationConfigHostGceInstanceShieldedInstanceConfigArgsDict(TypedDict):
    enable_integrity_monitoring: NotRequired[pulumi.Input[_builtins.bool]]
    enable_secure_boot: NotRequired[pulumi.Input[_builtins.bool]]
    enable_vtpm: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class WorkstationConfigHostGceInstanceShieldedInstanceConfigArgs:
    def __init__(__self__, *, enable_integrity_monitoring: Optional[pulumi.Input[_builtins.bool]] = ..., enable_secure_boot: Optional[pulumi.Input[_builtins.bool]] = ..., enable_vtpm: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableIntegrityMonitoring")
    def enable_integrity_monitoring(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_integrity_monitoring.setter
    def enable_integrity_monitoring(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSecureBoot")
    def enable_secure_boot(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_secure_boot.setter
    def enable_secure_boot(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableVtpm")
    def enable_vtpm(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_vtpm.setter
    def enable_vtpm(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class WorkstationConfigIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigPersistentDirectoryArgsDict(TypedDict):
    gce_pd: NotRequired[pulumi.Input[WorkstationConfigPersistentDirectoryGcePdArgsDict]]
    mount_path: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigPersistentDirectoryArgs:
    def __init__(__self__, *, gce_pd: Optional[pulumi.Input[WorkstationConfigPersistentDirectoryGcePdArgs]] = ..., mount_path: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcePd")
    def gce_pd(self) -> Optional[pulumi.Input[WorkstationConfigPersistentDirectoryGcePdArgs]]:
        
        ...
    
    @gce_pd.setter
    def gce_pd(self, value: Optional[pulumi.Input[WorkstationConfigPersistentDirectoryGcePdArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @mount_path.setter
    def mount_path(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigPersistentDirectoryGcePdArgsDict(TypedDict):
    disk_type: NotRequired[pulumi.Input[_builtins.str]]
    fs_type: NotRequired[pulumi.Input[_builtins.str]]
    reclaim_policy: NotRequired[pulumi.Input[_builtins.str]]
    size_gb: NotRequired[pulumi.Input[_builtins.int]]
    source_snapshot: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationConfigPersistentDirectoryGcePdArgs:
    def __init__(__self__, *, disk_type: Optional[pulumi.Input[_builtins.str]] = ..., fs_type: Optional[pulumi.Input[_builtins.str]] = ..., reclaim_policy: Optional[pulumi.Input[_builtins.str]] = ..., size_gb: Optional[pulumi.Input[_builtins.int]] = ..., source_snapshot: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="diskType")
    def disk_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @disk_type.setter
    def disk_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fsType")
    def fs_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @fs_type.setter
    def fs_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @reclaim_policy.setter
    def reclaim_policy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sizeGb")
    def size_gb(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @size_gb.setter
    def size_gb(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceSnapshot")
    def source_snapshot(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @source_snapshot.setter
    def source_snapshot(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationConfigReadinessCheckArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]


@pulumi.input_type
class WorkstationConfigReadinessCheckArgs:
    def __init__(__self__, *, path: pulumi.Input[_builtins.str], port: pulumi.Input[_builtins.int]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]:
        
        ...
    
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): # -> None:
        ...
    


class WorkstationIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationIamBindingConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class WorkstationIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class WorkstationIamMemberConditionArgs:
    def __init__(__self__, *, expression: pulumi.Input[_builtins.str], title: pulumi.Input[_builtins.str], description: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]:
        ...
    
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


