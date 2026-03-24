import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FilterFilterCriteria",
    "FilterFilterCriteriaAwsAccountId",
    "FilterFilterCriteriaCodeRepositoryProjectName",
    "FilterFilterCriteriaCodeRepositoryProviderType",
    "FilterFilterCriteriaCodeVulnerabilityDetectorName",
    "FilterFilterCriteriaCodeVulnerabilityDetectorTag",
    "FilterFilterCriteriaCodeVulnerabilityFilePath",
    "FilterFilterCriteriaComponentId",
    "FilterFilterCriteriaComponentType",
    "FilterFilterCriteriaEc2InstanceImageId",
    "FilterFilterCriteriaEc2InstanceSubnetId",
    "FilterFilterCriteriaEc2InstanceVpcId",
    "FilterFilterCriteriaEcrImageArchitecture",
    "FilterFilterCriteriaEcrImageHash",
    "FilterFilterCriteriaEcrImageInUseCount",
    "FilterFilterCriteriaEcrImageLastInUseAt",
    "FilterFilterCriteriaEcrImagePushedAt",
    "FilterFilterCriteriaEcrImageRegistry",
    "FilterFilterCriteriaEcrImageRepositoryName",
    "FilterFilterCriteriaEcrImageTag",
    "FilterFilterCriteriaEpssScore",
    "FilterFilterCriteriaExploitAvailable",
    "FilterFilterCriteriaFindingArn",
    "FilterFilterCriteriaFindingStatus",
    "FilterFilterCriteriaFindingType",
    "FilterFilterCriteriaFirstObservedAt",
    "FilterFilterCriteriaFixAvailable",
    "FilterFilterCriteriaInspectorScore",
    "FilterFilterCriteriaLambdaFunctionExecutionRoleArn",
    "FilterFilterCriteriaLambdaFunctionLastModifiedAt",
    "FilterFilterCriteriaLambdaFunctionLayer",
    "FilterFilterCriteriaLambdaFunctionName",
    "FilterFilterCriteriaLambdaFunctionRuntime",
    "FilterFilterCriteriaLastObservedAt",
    "FilterFilterCriteriaNetworkProtocol",
    "FilterFilterCriteriaPortRange",
    "FilterFilterCriteriaRelatedVulnerability",
    "FilterFilterCriteriaResourceId",
    "FilterFilterCriteriaResourceTag",
    "FilterFilterCriteriaResourceType",
    "FilterFilterCriteriaSeverity",
    "FilterFilterCriteriaTitle",
    "FilterFilterCriteriaUpdatedAt",
    "FilterFilterCriteriaVendorSeverity",
    "FilterFilterCriteriaVulnerabilityId",
    "FilterFilterCriteriaVulnerabilitySource",
    "FilterFilterCriteriaVulnerablePackage",
    "FilterFilterCriteriaVulnerablePackageArchitecture",
    "FilterFilterCriteriaVulnerablePackageEpoch",
    "FilterFilterCriteriaVulnerablePackageFilePath",
    "FilterFilterCriteriaVulnerablePackageName",
    "FilterFilterCriteriaVulnerablePackageRelease",
    ...,
    ...,
    "FilterFilterCriteriaVulnerablePackageVersion",
    "OrganizationConfigurationAutoEnable",
]

@pulumi.output_type
class FilterFilterCriteria(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        aws_account_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaAwsAccountId]
        ] = ...,
        code_repository_project_names: Optional[
            Sequence[outputs.FilterFilterCriteriaCodeRepositoryProjectName]
        ] = ...,
        code_repository_provider_types: Optional[
            Sequence[outputs.FilterFilterCriteriaCodeRepositoryProviderType]
        ] = ...,
        code_vulnerability_detector_names: Optional[
            Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityDetectorName]
        ] = ...,
        code_vulnerability_detector_tags: Optional[
            Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityDetectorTag]
        ] = ...,
        code_vulnerability_file_paths: Optional[
            Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityFilePath]
        ] = ...,
        component_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaComponentId]
        ] = ...,
        component_types: Optional[
            Sequence[outputs.FilterFilterCriteriaComponentType]
        ] = ...,
        ec2_instance_image_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaEc2InstanceImageId]
        ] = ...,
        ec2_instance_subnet_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaEc2InstanceSubnetId]
        ] = ...,
        ec2_instance_vpc_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaEc2InstanceVpcId]
        ] = ...,
        ecr_image_architectures: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageArchitecture]
        ] = ...,
        ecr_image_hashes: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageHash]
        ] = ...,
        ecr_image_in_use_counts: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageInUseCount]
        ] = ...,
        ecr_image_last_in_use_ats: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageLastInUseAt]
        ] = ...,
        ecr_image_pushed_ats: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImagePushedAt]
        ] = ...,
        ecr_image_registries: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageRegistry]
        ] = ...,
        ecr_image_repository_names: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageRepositoryName]
        ] = ...,
        ecr_image_tags: Optional[
            Sequence[outputs.FilterFilterCriteriaEcrImageTag]
        ] = ...,
        epss_scores: Optional[Sequence[outputs.FilterFilterCriteriaEpssScore]] = ...,
        exploit_availables: Optional[
            Sequence[outputs.FilterFilterCriteriaExploitAvailable]
        ] = ...,
        finding_arns: Optional[Sequence[outputs.FilterFilterCriteriaFindingArn]] = ...,
        finding_statuses: Optional[
            Sequence[outputs.FilterFilterCriteriaFindingStatus]
        ] = ...,
        finding_types: Optional[
            Sequence[outputs.FilterFilterCriteriaFindingType]
        ] = ...,
        first_observed_ats: Optional[
            Sequence[outputs.FilterFilterCriteriaFirstObservedAt]
        ] = ...,
        fix_availables: Optional[
            Sequence[outputs.FilterFilterCriteriaFixAvailable]
        ] = ...,
        inspector_scores: Optional[
            Sequence[outputs.FilterFilterCriteriaInspectorScore]
        ] = ...,
        lambda_function_execution_role_arns: Optional[
            Sequence[outputs.FilterFilterCriteriaLambdaFunctionExecutionRoleArn]
        ] = ...,
        lambda_function_last_modified_ats: Optional[
            Sequence[outputs.FilterFilterCriteriaLambdaFunctionLastModifiedAt]
        ] = ...,
        lambda_function_layers: Optional[
            Sequence[outputs.FilterFilterCriteriaLambdaFunctionLayer]
        ] = ...,
        lambda_function_names: Optional[
            Sequence[outputs.FilterFilterCriteriaLambdaFunctionName]
        ] = ...,
        lambda_function_runtimes: Optional[
            Sequence[outputs.FilterFilterCriteriaLambdaFunctionRuntime]
        ] = ...,
        last_observed_ats: Optional[
            Sequence[outputs.FilterFilterCriteriaLastObservedAt]
        ] = ...,
        network_protocols: Optional[
            Sequence[outputs.FilterFilterCriteriaNetworkProtocol]
        ] = ...,
        port_ranges: Optional[Sequence[outputs.FilterFilterCriteriaPortRange]] = ...,
        related_vulnerabilities: Optional[
            Sequence[outputs.FilterFilterCriteriaRelatedVulnerability]
        ] = ...,
        resource_ids: Optional[Sequence[outputs.FilterFilterCriteriaResourceId]] = ...,
        resource_tags: Optional[
            Sequence[outputs.FilterFilterCriteriaResourceTag]
        ] = ...,
        resource_types: Optional[
            Sequence[outputs.FilterFilterCriteriaResourceType]
        ] = ...,
        severities: Optional[Sequence[outputs.FilterFilterCriteriaSeverity]] = ...,
        titles: Optional[Sequence[outputs.FilterFilterCriteriaTitle]] = ...,
        updated_ats: Optional[Sequence[outputs.FilterFilterCriteriaUpdatedAt]] = ...,
        vendor_severities: Optional[
            Sequence[outputs.FilterFilterCriteriaVendorSeverity]
        ] = ...,
        vulnerability_ids: Optional[
            Sequence[outputs.FilterFilterCriteriaVulnerabilityId]
        ] = ...,
        vulnerability_sources: Optional[
            Sequence[outputs.FilterFilterCriteriaVulnerabilitySource]
        ] = ...,
        vulnerable_packages: Optional[
            Sequence[outputs.FilterFilterCriteriaVulnerablePackage]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaAwsAccountId]]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositoryProjectNames")
    def code_repository_project_names(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaCodeRepositoryProjectName]]: ...
    @_builtins.property
    @pulumi.getter(name="codeRepositoryProviderTypes")
    def code_repository_provider_types(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaCodeRepositoryProviderType]]: ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityDetectorNames")
    def code_vulnerability_detector_names(
        self,
    ) -> Optional[
        Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityDetectorName]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityDetectorTags")
    def code_vulnerability_detector_tags(
        self,
    ) -> Optional[
        Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityDetectorTag]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityFilePaths")
    def code_vulnerability_file_paths(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaCodeVulnerabilityFilePath]]: ...
    @_builtins.property
    @pulumi.getter(name="componentIds")
    def component_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaComponentId]]: ...
    @_builtins.property
    @pulumi.getter(name="componentTypes")
    def component_types(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaComponentType]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceImageIds")
    def ec2_instance_image_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEc2InstanceImageId]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceSubnetIds")
    def ec2_instance_subnet_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEc2InstanceSubnetId]]: ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceVpcIds")
    def ec2_instance_vpc_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEc2InstanceVpcId]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageArchitectures")
    def ecr_image_architectures(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageArchitecture]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageHashes")
    def ecr_image_hashes(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageHash]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageInUseCounts")
    def ecr_image_in_use_counts(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageInUseCount]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageLastInUseAts")
    def ecr_image_last_in_use_ats(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageLastInUseAt]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImagePushedAts")
    def ecr_image_pushed_ats(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImagePushedAt]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageRegistries")
    def ecr_image_registries(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageRegistry]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageRepositoryNames")
    def ecr_image_repository_names(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageRepositoryName]]: ...
    @_builtins.property
    @pulumi.getter(name="ecrImageTags")
    def ecr_image_tags(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEcrImageTag]]: ...
    @_builtins.property
    @pulumi.getter(name="epssScores")
    def epss_scores(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaEpssScore]]: ...
    @_builtins.property
    @pulumi.getter(name="exploitAvailables")
    def exploit_availables(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaExploitAvailable]]: ...
    @_builtins.property
    @pulumi.getter(name="findingArns")
    def finding_arns(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaFindingArn]]: ...
    @_builtins.property
    @pulumi.getter(name="findingStatuses")
    def finding_statuses(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaFindingStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="findingTypes")
    def finding_types(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaFindingType]]: ...
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaFirstObservedAt]]: ...
    @_builtins.property
    @pulumi.getter(name="fixAvailables")
    def fix_availables(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaFixAvailable]]: ...
    @_builtins.property
    @pulumi.getter(name="inspectorScores")
    def inspector_scores(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaInspectorScore]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionExecutionRoleArns")
    def lambda_function_execution_role_arns(
        self,
    ) -> Optional[
        Sequence[outputs.FilterFilterCriteriaLambdaFunctionExecutionRoleArn]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionLastModifiedAts")
    def lambda_function_last_modified_ats(
        self,
    ) -> Optional[
        Sequence[outputs.FilterFilterCriteriaLambdaFunctionLastModifiedAt]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionLayers")
    def lambda_function_layers(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaLambdaFunctionLayer]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionNames")
    def lambda_function_names(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaLambdaFunctionName]]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionRuntimes")
    def lambda_function_runtimes(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaLambdaFunctionRuntime]]: ...
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaLastObservedAt]]: ...
    @_builtins.property
    @pulumi.getter(name="networkProtocols")
    def network_protocols(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaNetworkProtocol]]: ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaPortRange]]: ...
    @_builtins.property
    @pulumi.getter(name="relatedVulnerabilities")
    def related_vulnerabilities(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaRelatedVulnerability]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaResourceId]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaResourceTag]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaResourceType]]: ...
    @_builtins.property
    @pulumi.getter
    def severities(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaSeverity]]: ...
    @_builtins.property
    @pulumi.getter
    def titles(self) -> Optional[Sequence[outputs.FilterFilterCriteriaTitle]]: ...
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaUpdatedAt]]: ...
    @_builtins.property
    @pulumi.getter(name="vendorSeverities")
    def vendor_severities(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaVendorSeverity]]: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityIds")
    def vulnerability_ids(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaVulnerabilityId]]: ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilitySources")
    def vulnerability_sources(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaVulnerabilitySource]]: ...
    @_builtins.property
    @pulumi.getter(name="vulnerablePackages")
    def vulnerable_packages(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaVulnerablePackage]]: ...

@pulumi.output_type
class FilterFilterCriteriaAwsAccountId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaCodeRepositoryProjectName(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaCodeRepositoryProviderType(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaCodeVulnerabilityDetectorName(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaCodeVulnerabilityDetectorTag(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaCodeVulnerabilityFilePath(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaComponentId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaComponentType(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEc2InstanceImageId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEc2InstanceSubnetId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEc2InstanceVpcId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageArchitecture(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageHash(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageInUseCount(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, lower_inclusive: _builtins.float, upper_inclusive: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> _builtins.float: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageLastInUseAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImagePushedAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageRegistry(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageRepositoryName(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEcrImageTag(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaEpssScore(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, lower_inclusive: _builtins.float, upper_inclusive: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> _builtins.float: ...

@pulumi.output_type
class FilterFilterCriteriaExploitAvailable(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaFindingArn(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaFindingStatus(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaFindingType(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaFirstObservedAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaFixAvailable(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaInspectorScore(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, lower_inclusive: _builtins.float, upper_inclusive: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> _builtins.float: ...

@pulumi.output_type
class FilterFilterCriteriaLambdaFunctionExecutionRoleArn(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaLambdaFunctionLastModifiedAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaLambdaFunctionLayer(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaLambdaFunctionName(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaLambdaFunctionRuntime(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaLastObservedAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaNetworkProtocol(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaPortRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, begin_inclusive: _builtins.int, end_inclusive: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="beginInclusive")
    def begin_inclusive(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> _builtins.int: ...

@pulumi.output_type
class FilterFilterCriteriaRelatedVulnerability(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaResourceId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaResourceTag(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, key: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaResourceType(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaSeverity(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaTitle(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaUpdatedAt(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[_builtins.str] = ...,
        start_inclusive: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FilterFilterCriteriaVendorSeverity(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerabilityId(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerabilitySource(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        architecture: Optional[
            outputs.FilterFilterCriteriaVulnerablePackageArchitecture
        ] = ...,
        epoches: Optional[
            Sequence[outputs.FilterFilterCriteriaVulnerablePackageEpoch]
        ] = ...,
        file_path: Optional[
            outputs.FilterFilterCriteriaVulnerablePackageFilePath
        ] = ...,
        name: Optional[outputs.FilterFilterCriteriaVulnerablePackageName] = ...,
        release: Optional[outputs.FilterFilterCriteriaVulnerablePackageRelease] = ...,
        source_lambda_layer_arn: Optional[
            outputs.FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArn
        ] = ...,
        source_layer_hash: Optional[
            outputs.FilterFilterCriteriaVulnerablePackageSourceLayerHash
        ] = ...,
        version: Optional[outputs.FilterFilterCriteriaVulnerablePackageVersion] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(
        self,
    ) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageArchitecture]: ...
    @_builtins.property
    @pulumi.getter
    def epoches(
        self,
    ) -> Optional[Sequence[outputs.FilterFilterCriteriaVulnerablePackageEpoch]]: ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(
        self,
    ) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageFilePath]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageName]: ...
    @_builtins.property
    @pulumi.getter
    def release(
        self,
    ) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageRelease]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLambdaLayerArn")
    def source_lambda_layer_arn(
        self,
    ) -> Optional[
        outputs.FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArn
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sourceLayerHash")
    def source_layer_hash(
        self,
    ) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageSourceLayerHash]: ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[outputs.FilterFilterCriteriaVulnerablePackageVersion]: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageArchitecture(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageEpoch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, lower_inclusive: _builtins.float, upper_inclusive: _builtins.float
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> _builtins.float: ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> _builtins.float: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageFilePath(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageName(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageRelease(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArn(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageSourceLayerHash(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FilterFilterCriteriaVulnerablePackageVersion(dict):
    def __init__(
        __self__, *, comparison: _builtins.str, value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class OrganizationConfigurationAutoEnable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ec2: _builtins.bool,
        ecr: _builtins.bool,
        code_repository: Optional[_builtins.bool] = ...,
        lambda_: Optional[_builtins.bool] = ...,
        lambda_code: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ec2(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def ecr(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="codeRepository")
    def code_repository(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="lambdaCode")
    def lambda_code(self) -> Optional[_builtins.bool]: ...
