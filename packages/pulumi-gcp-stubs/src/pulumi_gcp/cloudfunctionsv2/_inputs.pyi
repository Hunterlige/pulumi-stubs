import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FunctionBuildConfigArgs",
    "FunctionBuildConfigArgsDict",
    "FunctionBuildConfigAutomaticUpdatePolicyArgs",
    "FunctionBuildConfigAutomaticUpdatePolicyArgsDict",
    "FunctionBuildConfigOnDeployUpdatePolicyArgs",
    "FunctionBuildConfigOnDeployUpdatePolicyArgsDict",
    "FunctionBuildConfigSourceArgs",
    "FunctionBuildConfigSourceArgsDict",
    "FunctionBuildConfigSourceRepoSourceArgs",
    "FunctionBuildConfigSourceRepoSourceArgsDict",
    "FunctionBuildConfigSourceStorageSourceArgs",
    "FunctionBuildConfigSourceStorageSourceArgsDict",
    "FunctionEventTriggerArgs",
    "FunctionEventTriggerArgsDict",
    "FunctionEventTriggerEventFilterArgs",
    "FunctionEventTriggerEventFilterArgsDict",
    "FunctionIamBindingConditionArgs",
    "FunctionIamBindingConditionArgsDict",
    "FunctionIamMemberConditionArgs",
    "FunctionIamMemberConditionArgsDict",
    "FunctionServiceConfigArgs",
    "FunctionServiceConfigArgsDict",
    "FunctionServiceConfigDirectVpcNetworkInterfaceArgs",
    ...,
    "FunctionServiceConfigSecretEnvironmentVariableArgs",
    ...,
    "FunctionServiceConfigSecretVolumeArgs",
    "FunctionServiceConfigSecretVolumeArgsDict",
    "FunctionServiceConfigSecretVolumeVersionArgs",
    "FunctionServiceConfigSecretVolumeVersionArgsDict",
]

class FunctionBuildConfigArgsDict(TypedDict):
    automatic_update_policy: NotRequired[
        pulumi.Input[FunctionBuildConfigAutomaticUpdatePolicyArgsDict]
    ]
    build: NotRequired[pulumi.Input[_builtins.str]]
    docker_repository: NotRequired[pulumi.Input[_builtins.str]]
    entry_point: NotRequired[pulumi.Input[_builtins.str]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    on_deploy_update_policy: NotRequired[
        pulumi.Input[FunctionBuildConfigOnDeployUpdatePolicyArgsDict]
    ]
    runtime: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    source: NotRequired[pulumi.Input[FunctionBuildConfigSourceArgsDict]]
    worker_pool: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionBuildConfigArgs:
    def __init__(
        __self__,
        *,
        automatic_update_policy: Optional[
            pulumi.Input[FunctionBuildConfigAutomaticUpdatePolicyArgs]
        ] = ...,
        build: Optional[pulumi.Input[_builtins.str]] = ...,
        docker_repository: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_point: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        on_deploy_update_policy: Optional[
            pulumi.Input[FunctionBuildConfigOnDeployUpdatePolicyArgs]
        ] = ...,
        runtime: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[pulumi.Input[FunctionBuildConfigSourceArgs]] = ...,
        worker_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="automaticUpdatePolicy")
    def automatic_update_policy(
        self,
    ) -> Optional[pulumi.Input[FunctionBuildConfigAutomaticUpdatePolicyArgs]]: ...
    @automatic_update_policy.setter
    def automatic_update_policy(
        self,
        value: Optional[pulumi.Input[FunctionBuildConfigAutomaticUpdatePolicyArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @build.setter
    def build(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dockerRepository")
    def docker_repository(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @docker_repository.setter
    def docker_repository(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_point.setter
    def entry_point(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="onDeployUpdatePolicy")
    def on_deploy_update_policy(
        self,
    ) -> Optional[pulumi.Input[FunctionBuildConfigOnDeployUpdatePolicyArgs]]: ...
    @on_deploy_update_policy.setter
    def on_deploy_update_policy(
        self, value: Optional[pulumi.Input[FunctionBuildConfigOnDeployUpdatePolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def runtime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime.setter
    def runtime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[FunctionBuildConfigSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[FunctionBuildConfigSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_pool.setter
    def worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionBuildConfigAutomaticUpdatePolicyArgsDict(TypedDict): ...

@pulumi.input_type
class FunctionBuildConfigAutomaticUpdatePolicyArgs:
    def __init__(__self__) -> None: ...

class FunctionBuildConfigOnDeployUpdatePolicyArgsDict(TypedDict):
    runtime_version: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionBuildConfigOnDeployUpdatePolicyArgs:
    def __init__(
        __self__, *, runtime_version: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @runtime_version.setter
    def runtime_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionBuildConfigSourceArgsDict(TypedDict):
    repo_source: NotRequired[pulumi.Input[FunctionBuildConfigSourceRepoSourceArgsDict]]
    storage_source: NotRequired[
        pulumi.Input[FunctionBuildConfigSourceStorageSourceArgsDict]
    ]
    ...

@pulumi.input_type
class FunctionBuildConfigSourceArgs:
    def __init__(
        __self__,
        *,
        repo_source: Optional[
            pulumi.Input[FunctionBuildConfigSourceRepoSourceArgs]
        ] = ...,
        storage_source: Optional[
            pulumi.Input[FunctionBuildConfigSourceStorageSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="repoSource")
    def repo_source(
        self,
    ) -> Optional[pulumi.Input[FunctionBuildConfigSourceRepoSourceArgs]]: ...
    @repo_source.setter
    def repo_source(
        self, value: Optional[pulumi.Input[FunctionBuildConfigSourceRepoSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageSource")
    def storage_source(
        self,
    ) -> Optional[pulumi.Input[FunctionBuildConfigSourceStorageSourceArgs]]: ...
    @storage_source.setter
    def storage_source(
        self, value: Optional[pulumi.Input[FunctionBuildConfigSourceStorageSourceArgs]]
    ): ...

class FunctionBuildConfigSourceRepoSourceArgsDict(TypedDict):
    branch_name: NotRequired[pulumi.Input[_builtins.str]]
    commit_sha: NotRequired[pulumi.Input[_builtins.str]]
    dir: NotRequired[pulumi.Input[_builtins.str]]
    invert_regex: NotRequired[pulumi.Input[_builtins.bool]]
    project_id: NotRequired[pulumi.Input[_builtins.str]]
    repo_name: NotRequired[pulumi.Input[_builtins.str]]
    tag_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionBuildConfigSourceRepoSourceArgs:
    def __init__(
        __self__,
        *,
        branch_name: Optional[pulumi.Input[_builtins.str]] = ...,
        commit_sha: Optional[pulumi.Input[_builtins.str]] = ...,
        dir: Optional[pulumi.Input[_builtins.str]] = ...,
        invert_regex: Optional[pulumi.Input[_builtins.bool]] = ...,
        project_id: Optional[pulumi.Input[_builtins.str]] = ...,
        repo_name: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dir.setter
    def dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="invertRegex")
    def invert_regex(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invert_regex.setter
    def invert_regex(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @repo_name.setter
    def repo_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagName")
    def tag_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_name.setter
    def tag_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionBuildConfigSourceStorageSourceArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    generation: NotRequired[pulumi.Input[_builtins.int]]
    object: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionBuildConfigSourceStorageSourceArgs:
    def __init__(
        __self__,
        *,
        bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        generation: Optional[pulumi.Input[_builtins.int]] = ...,
        object: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object.setter
    def object(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionEventTriggerArgsDict(TypedDict):
    event_type: pulumi.Input[_builtins.str]
    event_filters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FunctionEventTriggerEventFilterArgsDict]]]
    ]
    pubsub_topic: NotRequired[pulumi.Input[_builtins.str]]
    retry_policy: NotRequired[pulumi.Input[_builtins.str]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    trigger: NotRequired[pulumi.Input[_builtins.str]]
    trigger_region: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionEventTriggerArgs:
    def __init__(
        __self__,
        *,
        event_type: pulumi.Input[_builtins.str],
        event_filters: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionEventTriggerEventFilterArgs]]]
        ] = ...,
        pubsub_topic: Optional[pulumi.Input[_builtins.str]] = ...,
        retry_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger: Optional[pulumi.Input[_builtins.str]] = ...,
        trigger_region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[_builtins.str]: ...
    @event_type.setter
    def event_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="eventFilters")
    def event_filters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FunctionEventTriggerEventFilterArgs]]]
    ]: ...
    @event_filters.setter
    def event_filters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionEventTriggerEventFilterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def trigger(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger.setter
    def trigger(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="triggerRegion")
    def trigger_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @trigger_region.setter
    def trigger_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionEventTriggerEventFilterArgsDict(TypedDict):
    attribute: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    operator: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionEventTriggerEventFilterArgs:
    def __init__(
        __self__,
        *,
        attribute: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
        operator: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def attribute(self) -> pulumi.Input[_builtins.str]: ...
    @attribute.setter
    def attribute(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @operator.setter
    def operator(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FunctionServiceConfigArgsDict(TypedDict):
    all_traffic_on_latest_revision: NotRequired[pulumi.Input[_builtins.bool]]
    available_cpu: NotRequired[pulumi.Input[_builtins.str]]
    available_memory: NotRequired[pulumi.Input[_builtins.str]]
    binary_authorization_policy: NotRequired[pulumi.Input[_builtins.str]]
    direct_vpc_egress: NotRequired[pulumi.Input[_builtins.str]]
    direct_vpc_network_interfaces: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FunctionServiceConfigDirectVpcNetworkInterfaceArgsDict]
            ]
        ]
    ]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    gcf_uri: NotRequired[pulumi.Input[_builtins.str]]
    ingress_settings: NotRequired[pulumi.Input[_builtins.str]]
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    max_instance_request_concurrency: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    secret_environment_variables: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FunctionServiceConfigSecretEnvironmentVariableArgsDict]
            ]
        ]
    ]
    secret_volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeArgsDict]]]
    ]
    service: NotRequired[pulumi.Input[_builtins.str]]
    service_account_email: NotRequired[pulumi.Input[_builtins.str]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    uri: NotRequired[pulumi.Input[_builtins.str]]
    vpc_connector: NotRequired[pulumi.Input[_builtins.str]]
    vpc_connector_egress_settings: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FunctionServiceConfigArgs:
    def __init__(
        __self__,
        *,
        all_traffic_on_latest_revision: Optional[pulumi.Input[_builtins.bool]] = ...,
        available_cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        available_memory: Optional[pulumi.Input[_builtins.str]] = ...,
        binary_authorization_policy: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_vpc_egress: Optional[pulumi.Input[_builtins.str]] = ...,
        direct_vpc_network_interfaces: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FunctionServiceConfigDirectVpcNetworkInterfaceArgs]
                ]
            ]
        ] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        gcf_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        ingress_settings: Optional[pulumi.Input[_builtins.str]] = ...,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_instance_request_concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        secret_environment_variables: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FunctionServiceConfigSecretEnvironmentVariableArgs]
                ]
            ]
        ] = ...,
        secret_volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeArgs]]]
        ] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account_email: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connector: Optional[pulumi.Input[_builtins.str]] = ...,
        vpc_connector_egress_settings: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allTrafficOnLatestRevision")
    def all_traffic_on_latest_revision(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @all_traffic_on_latest_revision.setter
    def all_traffic_on_latest_revision(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="availableCpu")
    def available_cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_cpu.setter
    def available_cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="availableMemory")
    def available_memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @available_memory.setter
    def available_memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationPolicy")
    def binary_authorization_policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @binary_authorization_policy.setter
    def binary_authorization_policy(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="directVpcEgress")
    def direct_vpc_egress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direct_vpc_egress.setter
    def direct_vpc_egress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="directVpcNetworkInterfaces")
    def direct_vpc_network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FunctionServiceConfigDirectVpcNetworkInterfaceArgs]]
        ]
    ]: ...
    @direct_vpc_network_interfaces.setter
    def direct_vpc_network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FunctionServiceConfigDirectVpcNetworkInterfaceArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gcfUri")
    def gcf_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcf_uri.setter
    def gcf_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ingressSettings")
    def ingress_settings(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ingress_settings.setter
    def ingress_settings(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_request_concurrency.setter
    def max_instance_request_concurrency(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="secretEnvironmentVariables")
    def secret_environment_variables(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FunctionServiceConfigSecretEnvironmentVariableArgs]]
        ]
    ]: ...
    @secret_environment_variables.setter
    def secret_environment_variables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FunctionServiceConfigSecretEnvironmentVariableArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretVolumes")
    def secret_volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeArgs]]]
    ]: ...
    @secret_volumes.setter
    def secret_volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountEmail")
    def service_account_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account_email.setter
    def service_account_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConnector")
    def vpc_connector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_connector.setter
    def vpc_connector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectorEgressSettings")
    def vpc_connector_egress_settings(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @vpc_connector_egress_settings.setter
    def vpc_connector_egress_settings(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class FunctionServiceConfigDirectVpcNetworkInterfaceArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class FunctionServiceConfigDirectVpcNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class FunctionServiceConfigSecretEnvironmentVariableArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    secret: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FunctionServiceConfigSecretEnvironmentVariableArgs:
    def __init__(
        __self__,
        *,
        key: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        secret: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...

class FunctionServiceConfigSecretVolumeArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    project_id: pulumi.Input[_builtins.str]
    secret: pulumi.Input[_builtins.str]
    versions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeVersionArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class FunctionServiceConfigSecretVolumeArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        project_id: pulumi.Input[_builtins.str],
        secret: pulumi.Input[_builtins.str],
        versions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeVersionArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[_builtins.str]: ...
    @project_id.setter
    def project_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def versions(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeVersionArgs]]
        ]
    ]: ...
    @versions.setter
    def versions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FunctionServiceConfigSecretVolumeVersionArgs]]
            ]
        ],
    ): ...

class FunctionServiceConfigSecretVolumeVersionArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FunctionServiceConfigSecretVolumeVersionArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
