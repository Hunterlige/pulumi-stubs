import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "FilterFilterCriteriaArgs",
    "FilterFilterCriteriaArgsDict",
    "FilterFilterCriteriaAwsAccountIdArgs",
    "FilterFilterCriteriaAwsAccountIdArgsDict",
    "FilterFilterCriteriaCodeRepositoryProjectNameArgs",
    ...,
    "FilterFilterCriteriaCodeRepositoryProviderTypeArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "FilterFilterCriteriaCodeVulnerabilityFilePathArgs",
    ...,
    "FilterFilterCriteriaComponentIdArgs",
    "FilterFilterCriteriaComponentIdArgsDict",
    "FilterFilterCriteriaComponentTypeArgs",
    "FilterFilterCriteriaComponentTypeArgsDict",
    "FilterFilterCriteriaEc2InstanceImageIdArgs",
    "FilterFilterCriteriaEc2InstanceImageIdArgsDict",
    "FilterFilterCriteriaEc2InstanceSubnetIdArgs",
    "FilterFilterCriteriaEc2InstanceSubnetIdArgsDict",
    "FilterFilterCriteriaEc2InstanceVpcIdArgs",
    "FilterFilterCriteriaEc2InstanceVpcIdArgsDict",
    "FilterFilterCriteriaEcrImageArchitectureArgs",
    "FilterFilterCriteriaEcrImageArchitectureArgsDict",
    "FilterFilterCriteriaEcrImageHashArgs",
    "FilterFilterCriteriaEcrImageHashArgsDict",
    "FilterFilterCriteriaEcrImageInUseCountArgs",
    "FilterFilterCriteriaEcrImageInUseCountArgsDict",
    "FilterFilterCriteriaEcrImageLastInUseAtArgs",
    "FilterFilterCriteriaEcrImageLastInUseAtArgsDict",
    "FilterFilterCriteriaEcrImagePushedAtArgs",
    "FilterFilterCriteriaEcrImagePushedAtArgsDict",
    "FilterFilterCriteriaEcrImageRegistryArgs",
    "FilterFilterCriteriaEcrImageRegistryArgsDict",
    "FilterFilterCriteriaEcrImageRepositoryNameArgs",
    "FilterFilterCriteriaEcrImageRepositoryNameArgsDict",
    "FilterFilterCriteriaEcrImageTagArgs",
    "FilterFilterCriteriaEcrImageTagArgsDict",
    "FilterFilterCriteriaEpssScoreArgs",
    "FilterFilterCriteriaEpssScoreArgsDict",
    "FilterFilterCriteriaExploitAvailableArgs",
    "FilterFilterCriteriaExploitAvailableArgsDict",
    "FilterFilterCriteriaFindingArnArgs",
    "FilterFilterCriteriaFindingArnArgsDict",
    "FilterFilterCriteriaFindingStatusArgs",
    "FilterFilterCriteriaFindingStatusArgsDict",
    "FilterFilterCriteriaFindingTypeArgs",
    "FilterFilterCriteriaFindingTypeArgsDict",
    "FilterFilterCriteriaFirstObservedAtArgs",
    "FilterFilterCriteriaFirstObservedAtArgsDict",
    "FilterFilterCriteriaFixAvailableArgs",
    "FilterFilterCriteriaFixAvailableArgsDict",
    "FilterFilterCriteriaInspectorScoreArgs",
    "FilterFilterCriteriaInspectorScoreArgsDict",
    ...,
    ...,
    ...,
    ...,
    "FilterFilterCriteriaLambdaFunctionLayerArgs",
    "FilterFilterCriteriaLambdaFunctionLayerArgsDict",
    "FilterFilterCriteriaLambdaFunctionNameArgs",
    "FilterFilterCriteriaLambdaFunctionNameArgsDict",
    "FilterFilterCriteriaLambdaFunctionRuntimeArgs",
    "FilterFilterCriteriaLambdaFunctionRuntimeArgsDict",
    "FilterFilterCriteriaLastObservedAtArgs",
    "FilterFilterCriteriaLastObservedAtArgsDict",
    "FilterFilterCriteriaNetworkProtocolArgs",
    "FilterFilterCriteriaNetworkProtocolArgsDict",
    "FilterFilterCriteriaPortRangeArgs",
    "FilterFilterCriteriaPortRangeArgsDict",
    "FilterFilterCriteriaRelatedVulnerabilityArgs",
    "FilterFilterCriteriaRelatedVulnerabilityArgsDict",
    "FilterFilterCriteriaResourceIdArgs",
    "FilterFilterCriteriaResourceIdArgsDict",
    "FilterFilterCriteriaResourceTagArgs",
    "FilterFilterCriteriaResourceTagArgsDict",
    "FilterFilterCriteriaResourceTypeArgs",
    "FilterFilterCriteriaResourceTypeArgsDict",
    "FilterFilterCriteriaSeverityArgs",
    "FilterFilterCriteriaSeverityArgsDict",
    "FilterFilterCriteriaTitleArgs",
    "FilterFilterCriteriaTitleArgsDict",
    "FilterFilterCriteriaUpdatedAtArgs",
    "FilterFilterCriteriaUpdatedAtArgsDict",
    "FilterFilterCriteriaVendorSeverityArgs",
    "FilterFilterCriteriaVendorSeverityArgsDict",
    "FilterFilterCriteriaVulnerabilityIdArgs",
    "FilterFilterCriteriaVulnerabilityIdArgsDict",
    "FilterFilterCriteriaVulnerabilitySourceArgs",
    "FilterFilterCriteriaVulnerabilitySourceArgsDict",
    "FilterFilterCriteriaVulnerablePackageArgs",
    "FilterFilterCriteriaVulnerablePackageArgsDict",
    ...,
    ...,
    "FilterFilterCriteriaVulnerablePackageEpochArgs",
    "FilterFilterCriteriaVulnerablePackageEpochArgsDict",
    "FilterFilterCriteriaVulnerablePackageFilePathArgs",
    ...,
    "FilterFilterCriteriaVulnerablePackageNameArgs",
    "FilterFilterCriteriaVulnerablePackageNameArgsDict",
    "FilterFilterCriteriaVulnerablePackageReleaseArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "FilterFilterCriteriaVulnerablePackageVersionArgs",
    ...,
    "OrganizationConfigurationAutoEnableArgs",
    "OrganizationConfigurationAutoEnableArgsDict",
]

class FilterFilterCriteriaArgsDict(TypedDict):
    aws_account_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaAwsAccountIdArgsDict]]]
    ]
    code_repository_project_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeRepositoryProjectNameArgsDict]
            ]
        ]
    ]
    code_repository_provider_types: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeRepositoryProviderTypeArgsDict]
            ]
        ]
    ]
    code_vulnerability_detector_names: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorNameArgsDict]
            ]
        ]
    ]
    code_vulnerability_detector_tags: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorTagArgsDict]
            ]
        ]
    ]
    code_vulnerability_file_paths: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeVulnerabilityFilePathArgsDict]
            ]
        ]
    ]
    component_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentIdArgsDict]]]
    ]
    component_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentTypeArgsDict]]]
    ]
    ec2_instance_image_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceImageIdArgsDict]]
        ]
    ]
    ec2_instance_subnet_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceSubnetIdArgsDict]]
        ]
    ]
    ec2_instance_vpc_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceVpcIdArgsDict]]
        ]
    ]
    ecr_image_architectures: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageArchitectureArgsDict]]
        ]
    ]
    ecr_image_hashes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageHashArgsDict]]]
    ]
    ecr_image_in_use_counts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageInUseCountArgsDict]]
        ]
    ]
    ecr_image_last_in_use_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageLastInUseAtArgsDict]]
        ]
    ]
    ecr_image_pushed_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImagePushedAtArgsDict]]
        ]
    ]
    ecr_image_registries: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRegistryArgsDict]]
        ]
    ]
    ecr_image_repository_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRepositoryNameArgsDict]]
        ]
    ]
    ecr_image_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageTagArgsDict]]]
    ]
    epss_scores: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEpssScoreArgsDict]]]
    ]
    exploit_availables: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaExploitAvailableArgsDict]]
        ]
    ]
    finding_arns: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingArnArgsDict]]]
    ]
    finding_statuses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingStatusArgsDict]]]
    ]
    finding_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingTypeArgsDict]]]
    ]
    first_observed_ats: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaFirstObservedAtArgsDict]]
        ]
    ]
    fix_availables: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFixAvailableArgsDict]]]
    ]
    inspector_scores: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaInspectorScoreArgsDict]]]
    ]
    lambda_function_execution_role_arns: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgsDict]
            ]
        ]
    ]
    lambda_function_last_modified_ats: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaLambdaFunctionLastModifiedAtArgsDict]
            ]
        ]
    ]
    lambda_function_layers: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionLayerArgsDict]]
        ]
    ]
    lambda_function_names: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionNameArgsDict]]
        ]
    ]
    lambda_function_runtimes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionRuntimeArgsDict]]
        ]
    ]
    last_observed_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaLastObservedAtArgsDict]]]
    ]
    network_protocols: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaNetworkProtocolArgsDict]]
        ]
    ]
    port_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaPortRangeArgsDict]]]
    ]
    related_vulnerabilities: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaRelatedVulnerabilityArgsDict]]
        ]
    ]
    resource_ids: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceIdArgsDict]]]
    ]
    resource_tags: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTagArgsDict]]]
    ]
    resource_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTypeArgsDict]]]
    ]
    severities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaSeverityArgsDict]]]
    ]
    titles: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaTitleArgsDict]]]
    ]
    updated_ats: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaUpdatedAtArgsDict]]]
    ]
    vendor_severities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVendorSeverityArgsDict]]]
    ]
    vulnerability_ids: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilityIdArgsDict]]
        ]
    ]
    vulnerability_sources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilitySourceArgsDict]]
        ]
    ]
    vulnerable_packages: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class FilterFilterCriteriaArgs:
    def __init__(
        __self__,
        *,
        aws_account_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaAwsAccountIdArgs]]]
        ] = ...,
        code_repository_project_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeRepositoryProjectNameArgs]
                ]
            ]
        ] = ...,
        code_repository_provider_types: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeRepositoryProviderTypeArgs]
                ]
            ]
        ] = ...,
        code_vulnerability_detector_names: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorNameArgs]
                ]
            ]
        ] = ...,
        code_vulnerability_detector_tags: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorTagArgs]
                ]
            ]
        ] = ...,
        code_vulnerability_file_paths: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityFilePathArgs]
                ]
            ]
        ] = ...,
        component_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentIdArgs]]]
        ] = ...,
        component_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentTypeArgs]]]
        ] = ...,
        ec2_instance_image_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceImageIdArgs]]
            ]
        ] = ...,
        ec2_instance_subnet_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceSubnetIdArgs]]
            ]
        ] = ...,
        ec2_instance_vpc_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceVpcIdArgs]]
            ]
        ] = ...,
        ecr_image_architectures: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageArchitectureArgs]]
            ]
        ] = ...,
        ecr_image_hashes: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageHashArgs]]]
        ] = ...,
        ecr_image_in_use_counts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageInUseCountArgs]]
            ]
        ] = ...,
        ecr_image_last_in_use_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageLastInUseAtArgs]]
            ]
        ] = ...,
        ecr_image_pushed_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImagePushedAtArgs]]
            ]
        ] = ...,
        ecr_image_registries: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRegistryArgs]]
            ]
        ] = ...,
        ecr_image_repository_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRepositoryNameArgs]]
            ]
        ] = ...,
        ecr_image_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageTagArgs]]]
        ] = ...,
        epss_scores: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEpssScoreArgs]]]
        ] = ...,
        exploit_availables: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaExploitAvailableArgs]]
            ]
        ] = ...,
        finding_arns: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingArnArgs]]]
        ] = ...,
        finding_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingStatusArgs]]]
        ] = ...,
        finding_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingTypeArgs]]]
        ] = ...,
        first_observed_ats: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaFirstObservedAtArgs]]
            ]
        ] = ...,
        fix_availables: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFixAvailableArgs]]]
        ] = ...,
        inspector_scores: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaInspectorScoreArgs]]]
        ] = ...,
        lambda_function_execution_role_arns: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgs]
                ]
            ]
        ] = ...,
        lambda_function_last_modified_ats: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaLambdaFunctionLastModifiedAtArgs]
                ]
            ]
        ] = ...,
        lambda_function_layers: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionLayerArgs]]
            ]
        ] = ...,
        lambda_function_names: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionNameArgs]]
            ]
        ] = ...,
        lambda_function_runtimes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionRuntimeArgs]]
            ]
        ] = ...,
        last_observed_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaLastObservedAtArgs]]]
        ] = ...,
        network_protocols: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaNetworkProtocolArgs]]
            ]
        ] = ...,
        port_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaPortRangeArgs]]]
        ] = ...,
        related_vulnerabilities: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaRelatedVulnerabilityArgs]]
            ]
        ] = ...,
        resource_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceIdArgs]]]
        ] = ...,
        resource_tags: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTagArgs]]]
        ] = ...,
        resource_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTypeArgs]]]
        ] = ...,
        severities: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaSeverityArgs]]]
        ] = ...,
        titles: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaTitleArgs]]]
        ] = ...,
        updated_ats: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaUpdatedAtArgs]]]
        ] = ...,
        vendor_severities: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVendorSeverityArgs]]]
        ] = ...,
        vulnerability_ids: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilityIdArgs]]
            ]
        ] = ...,
        vulnerability_sources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilitySourceArgs]]
            ]
        ] = ...,
        vulnerable_packages: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="awsAccountIds")
    def aws_account_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaAwsAccountIdArgs]]]
    ]: ...
    @aws_account_ids.setter
    def aws_account_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaAwsAccountIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeRepositoryProjectNames")
    def code_repository_project_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaCodeRepositoryProjectNameArgs]]
        ]
    ]: ...
    @code_repository_project_names.setter
    def code_repository_project_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeRepositoryProjectNameArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeRepositoryProviderTypes")
    def code_repository_provider_types(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaCodeRepositoryProviderTypeArgs]]
        ]
    ]: ...
    @code_repository_provider_types.setter
    def code_repository_provider_types(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeRepositoryProviderTypeArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityDetectorNames")
    def code_vulnerability_detector_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorNameArgs]
            ]
        ]
    ]: ...
    @code_vulnerability_detector_names.setter
    def code_vulnerability_detector_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorNameArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityDetectorTags")
    def code_vulnerability_detector_tags(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorTagArgs]]
        ]
    ]: ...
    @code_vulnerability_detector_tags.setter
    def code_vulnerability_detector_tags(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityDetectorTagArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeVulnerabilityFilePaths")
    def code_vulnerability_file_paths(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaCodeVulnerabilityFilePathArgs]]
        ]
    ]: ...
    @code_vulnerability_file_paths.setter
    def code_vulnerability_file_paths(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaCodeVulnerabilityFilePathArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="componentIds")
    def component_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentIdArgs]]]
    ]: ...
    @component_ids.setter
    def component_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="componentTypes")
    def component_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentTypeArgs]]]
    ]: ...
    @component_types.setter
    def component_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaComponentTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceImageIds")
    def ec2_instance_image_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceImageIdArgs]]]
    ]: ...
    @ec2_instance_image_ids.setter
    def ec2_instance_image_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceImageIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceSubnetIds")
    def ec2_instance_subnet_ids(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceSubnetIdArgs]]
        ]
    ]: ...
    @ec2_instance_subnet_ids.setter
    def ec2_instance_subnet_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceSubnetIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ec2InstanceVpcIds")
    def ec2_instance_vpc_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceVpcIdArgs]]]
    ]: ...
    @ec2_instance_vpc_ids.setter
    def ec2_instance_vpc_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEc2InstanceVpcIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageArchitectures")
    def ecr_image_architectures(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageArchitectureArgs]]
        ]
    ]: ...
    @ecr_image_architectures.setter
    def ecr_image_architectures(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageArchitectureArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageHashes")
    def ecr_image_hashes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageHashArgs]]]
    ]: ...
    @ecr_image_hashes.setter
    def ecr_image_hashes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageHashArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageInUseCounts")
    def ecr_image_in_use_counts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageInUseCountArgs]]]
    ]: ...
    @ecr_image_in_use_counts.setter
    def ecr_image_in_use_counts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageInUseCountArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageLastInUseAts")
    def ecr_image_last_in_use_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageLastInUseAtArgs]]
        ]
    ]: ...
    @ecr_image_last_in_use_ats.setter
    def ecr_image_last_in_use_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageLastInUseAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImagePushedAts")
    def ecr_image_pushed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImagePushedAtArgs]]]
    ]: ...
    @ecr_image_pushed_ats.setter
    def ecr_image_pushed_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImagePushedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageRegistries")
    def ecr_image_registries(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRegistryArgs]]]
    ]: ...
    @ecr_image_registries.setter
    def ecr_image_registries(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRegistryArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageRepositoryNames")
    def ecr_image_repository_names(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRepositoryNameArgs]]
        ]
    ]: ...
    @ecr_image_repository_names.setter
    def ecr_image_repository_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaEcrImageRepositoryNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ecrImageTags")
    def ecr_image_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageTagArgs]]]
    ]: ...
    @ecr_image_tags.setter
    def ecr_image_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEcrImageTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="epssScores")
    def epss_scores(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEpssScoreArgs]]]
    ]: ...
    @epss_scores.setter
    def epss_scores(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaEpssScoreArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exploitAvailables")
    def exploit_availables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaExploitAvailableArgs]]]
    ]: ...
    @exploit_availables.setter
    def exploit_availables(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaExploitAvailableArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingArns")
    def finding_arns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingArnArgs]]]
    ]: ...
    @finding_arns.setter
    def finding_arns(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingArnArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingStatuses")
    def finding_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingStatusArgs]]]
    ]: ...
    @finding_statuses.setter
    def finding_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="findingTypes")
    def finding_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingTypeArgs]]]
    ]: ...
    @finding_types.setter
    def finding_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFindingTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="firstObservedAts")
    def first_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFirstObservedAtArgs]]]
    ]: ...
    @first_observed_ats.setter
    def first_observed_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaFirstObservedAtArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fixAvailables")
    def fix_availables(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFixAvailableArgs]]]
    ]: ...
    @fix_availables.setter
    def fix_availables(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaFixAvailableArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inspectorScores")
    def inspector_scores(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaInspectorScoreArgs]]]
    ]: ...
    @inspector_scores.setter
    def inspector_scores(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaInspectorScoreArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionExecutionRoleArns")
    def lambda_function_execution_role_arns(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgs]
            ]
        ]
    ]: ...
    @lambda_function_execution_role_arns.setter
    def lambda_function_execution_role_arns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionLastModifiedAts")
    def lambda_function_last_modified_ats(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionLastModifiedAtArgs]]
        ]
    ]: ...
    @lambda_function_last_modified_ats.setter
    def lambda_function_last_modified_ats(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[FilterFilterCriteriaLambdaFunctionLastModifiedAtArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionLayers")
    def lambda_function_layers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionLayerArgs]]
        ]
    ]: ...
    @lambda_function_layers.setter
    def lambda_function_layers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionLayerArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionNames")
    def lambda_function_names(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionNameArgs]]]
    ]: ...
    @lambda_function_names.setter
    def lambda_function_names(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionNameArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lambdaFunctionRuntimes")
    def lambda_function_runtimes(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionRuntimeArgs]]
        ]
    ]: ...
    @lambda_function_runtimes.setter
    def lambda_function_runtimes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaLambdaFunctionRuntimeArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="lastObservedAts")
    def last_observed_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaLastObservedAtArgs]]]
    ]: ...
    @last_observed_ats.setter
    def last_observed_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaLastObservedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="networkProtocols")
    def network_protocols(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaNetworkProtocolArgs]]]
    ]: ...
    @network_protocols.setter
    def network_protocols(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaNetworkProtocolArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="portRanges")
    def port_ranges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaPortRangeArgs]]]
    ]: ...
    @port_ranges.setter
    def port_ranges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaPortRangeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="relatedVulnerabilities")
    def related_vulnerabilities(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaRelatedVulnerabilityArgs]]
        ]
    ]: ...
    @related_vulnerabilities.setter
    def related_vulnerabilities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaRelatedVulnerabilityArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceIds")
    def resource_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceIdArgs]]]
    ]: ...
    @resource_ids.setter
    def resource_ids(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceIdArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTags")
    def resource_tags(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTagArgs]]]
    ]: ...
    @resource_tags.setter
    def resource_tags(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTagArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceTypes")
    def resource_types(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTypeArgs]]]
    ]: ...
    @resource_types.setter
    def resource_types(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaResourceTypeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def severities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaSeverityArgs]]]
    ]: ...
    @severities.setter
    def severities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaSeverityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def titles(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaTitleArgs]]]
    ]: ...
    @titles.setter
    def titles(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaTitleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updatedAts")
    def updated_ats(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaUpdatedAtArgs]]]
    ]: ...
    @updated_ats.setter
    def updated_ats(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaUpdatedAtArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vendorSeverities")
    def vendor_severities(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVendorSeverityArgs]]]
    ]: ...
    @vendor_severities.setter
    def vendor_severities(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVendorSeverityArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilityIds")
    def vulnerability_ids(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilityIdArgs]]]
    ]: ...
    @vulnerability_ids.setter
    def vulnerability_ids(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilityIdArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vulnerabilitySources")
    def vulnerability_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilitySourceArgs]]
        ]
    ]: ...
    @vulnerability_sources.setter
    def vulnerability_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerabilitySourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vulnerablePackages")
    def vulnerable_packages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageArgs]]]
    ]: ...
    @vulnerable_packages.setter
    def vulnerable_packages(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageArgs]]
            ]
        ],
    ): ...

class FilterFilterCriteriaAwsAccountIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaAwsAccountIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaCodeRepositoryProjectNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaCodeRepositoryProjectNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaCodeRepositoryProviderTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaCodeRepositoryProviderTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaCodeVulnerabilityDetectorNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaCodeVulnerabilityDetectorNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaCodeVulnerabilityDetectorTagArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaCodeVulnerabilityDetectorTagArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaCodeVulnerabilityFilePathArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaCodeVulnerabilityFilePathArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaComponentIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaComponentIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaComponentTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaComponentTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEc2InstanceImageIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEc2InstanceImageIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEc2InstanceSubnetIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEc2InstanceSubnetIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEc2InstanceVpcIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEc2InstanceVpcIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEcrImageArchitectureArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageArchitectureArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEcrImageHashArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageHashArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEcrImageInUseCountArgsDict(TypedDict):
    lower_inclusive: pulumi.Input[_builtins.float]
    upper_inclusive: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageInUseCountArgs:
    def __init__(
        __self__,
        *,
        lower_inclusive: pulumi.Input[_builtins.float],
        upper_inclusive: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @lower_inclusive.setter
    def lower_inclusive(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @upper_inclusive.setter
    def upper_inclusive(self, value: pulumi.Input[_builtins.float]): ...

class FilterFilterCriteriaEcrImageLastInUseAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageLastInUseAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaEcrImagePushedAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImagePushedAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaEcrImageRegistryArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageRegistryArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEcrImageRepositoryNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageRepositoryNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEcrImageTagArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaEcrImageTagArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaEpssScoreArgsDict(TypedDict):
    lower_inclusive: pulumi.Input[_builtins.float]
    upper_inclusive: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class FilterFilterCriteriaEpssScoreArgs:
    def __init__(
        __self__,
        *,
        lower_inclusive: pulumi.Input[_builtins.float],
        upper_inclusive: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @lower_inclusive.setter
    def lower_inclusive(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @upper_inclusive.setter
    def upper_inclusive(self, value: pulumi.Input[_builtins.float]): ...

class FilterFilterCriteriaExploitAvailableArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaExploitAvailableArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaFindingArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaFindingArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaFindingStatusArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaFindingStatusArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaFindingTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaFindingTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaFirstObservedAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaFirstObservedAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaFixAvailableArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaFixAvailableArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaInspectorScoreArgsDict(TypedDict):
    lower_inclusive: pulumi.Input[_builtins.float]
    upper_inclusive: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class FilterFilterCriteriaInspectorScoreArgs:
    def __init__(
        __self__,
        *,
        lower_inclusive: pulumi.Input[_builtins.float],
        upper_inclusive: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @lower_inclusive.setter
    def lower_inclusive(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @upper_inclusive.setter
    def upper_inclusive(self, value: pulumi.Input[_builtins.float]): ...

class FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaLambdaFunctionExecutionRoleArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaLambdaFunctionLastModifiedAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaLambdaFunctionLastModifiedAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaLambdaFunctionLayerArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaLambdaFunctionLayerArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaLambdaFunctionNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaLambdaFunctionNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaLambdaFunctionRuntimeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaLambdaFunctionRuntimeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaLastObservedAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaLastObservedAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaNetworkProtocolArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaNetworkProtocolArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaPortRangeArgsDict(TypedDict):
    begin_inclusive: pulumi.Input[_builtins.int]
    end_inclusive: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class FilterFilterCriteriaPortRangeArgs:
    def __init__(
        __self__,
        *,
        begin_inclusive: pulumi.Input[_builtins.int],
        end_inclusive: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="beginInclusive")
    def begin_inclusive(self) -> pulumi.Input[_builtins.int]: ...
    @begin_inclusive.setter
    def begin_inclusive(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> pulumi.Input[_builtins.int]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: pulumi.Input[_builtins.int]): ...

class FilterFilterCriteriaRelatedVulnerabilityArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaRelatedVulnerabilityArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaResourceIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaResourceIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaResourceTagArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaResourceTagArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaResourceTypeArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaResourceTypeArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaSeverityArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaSeverityArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaTitleArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaTitleArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaUpdatedAtArgsDict(TypedDict):
    end_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    start_inclusive: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class FilterFilterCriteriaUpdatedAtArgs:
    def __init__(
        __self__,
        *,
        end_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
        start_inclusive: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endInclusive")
    def end_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_inclusive.setter
    def end_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startInclusive")
    def start_inclusive(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_inclusive.setter
    def start_inclusive(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FilterFilterCriteriaVendorSeverityArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVendorSeverityArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerabilityIdArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerabilityIdArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerabilitySourceArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerabilitySourceArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageArgsDict(TypedDict):
    architecture: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageArchitectureArgsDict]
    ]
    epoches: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageEpochArgsDict]]
        ]
    ]
    file_path: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageFilePathArgsDict]
    ]
    name: NotRequired[pulumi.Input[FilterFilterCriteriaVulnerablePackageNameArgsDict]]
    release: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageReleaseArgsDict]
    ]
    source_lambda_layer_arn: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgsDict]
    ]
    source_layer_hash: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLayerHashArgsDict]
    ]
    version: NotRequired[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageVersionArgsDict]
    ]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageArgs:
    def __init__(
        __self__,
        *,
        architecture: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageArchitectureArgs]
        ] = ...,
        epoches: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageEpochArgs]]
            ]
        ] = ...,
        file_path: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageFilePathArgs]
        ] = ...,
        name: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageNameArgs]
        ] = ...,
        release: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageReleaseArgs]
        ] = ...,
        source_lambda_layer_arn: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgs]
        ] = ...,
        source_layer_hash: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLayerHashArgs]
        ] = ...,
        version: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageVersionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def architecture(
        self,
    ) -> Optional[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageArchitectureArgs]
    ]: ...
    @architecture.setter
    def architecture(
        self,
        value: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageArchitectureArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def epoches(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageEpochArgs]]
        ]
    ]: ...
    @epoches.setter
    def epoches(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FilterFilterCriteriaVulnerablePackageEpochArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filePath")
    def file_path(
        self,
    ) -> Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageFilePathArgs]]: ...
    @file_path.setter
    def file_path(
        self,
        value: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageFilePathArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(
        self,
    ) -> Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageNameArgs]]: ...
    @name.setter
    def name(
        self,
        value: Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageNameArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def release(
        self,
    ) -> Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageReleaseArgs]]: ...
    @release.setter
    def release(
        self,
        value: Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageReleaseArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceLambdaLayerArn")
    def source_lambda_layer_arn(
        self,
    ) -> Optional[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgs]
    ]: ...
    @source_lambda_layer_arn.setter
    def source_lambda_layer_arn(
        self,
        value: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceLayerHash")
    def source_layer_hash(
        self,
    ) -> Optional[
        pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLayerHashArgs]
    ]: ...
    @source_layer_hash.setter
    def source_layer_hash(
        self,
        value: Optional[
            pulumi.Input[FilterFilterCriteriaVulnerablePackageSourceLayerHashArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def version(
        self,
    ) -> Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageVersionArgs]]: ...
    @version.setter
    def version(
        self,
        value: Optional[pulumi.Input[FilterFilterCriteriaVulnerablePackageVersionArgs]],
    ): ...

class FilterFilterCriteriaVulnerablePackageArchitectureArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageArchitectureArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageEpochArgsDict(TypedDict):
    lower_inclusive: pulumi.Input[_builtins.float]
    upper_inclusive: pulumi.Input[_builtins.float]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageEpochArgs:
    def __init__(
        __self__,
        *,
        lower_inclusive: pulumi.Input[_builtins.float],
        upper_inclusive: pulumi.Input[_builtins.float],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lowerInclusive")
    def lower_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @lower_inclusive.setter
    def lower_inclusive(self, value: pulumi.Input[_builtins.float]): ...
    @_builtins.property
    @pulumi.getter(name="upperInclusive")
    def upper_inclusive(self) -> pulumi.Input[_builtins.float]: ...
    @upper_inclusive.setter
    def upper_inclusive(self, value: pulumi.Input[_builtins.float]): ...

class FilterFilterCriteriaVulnerablePackageFilePathArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageFilePathArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageNameArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageNameArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageReleaseArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageReleaseArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageSourceLambdaLayerArnArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageSourceLayerHashArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageSourceLayerHashArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class FilterFilterCriteriaVulnerablePackageVersionArgsDict(TypedDict):
    comparison: pulumi.Input[_builtins.str]
    value: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FilterFilterCriteriaVulnerablePackageVersionArgs:
    def __init__(
        __self__,
        *,
        comparison: pulumi.Input[_builtins.str],
        value: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def comparison(self) -> pulumi.Input[_builtins.str]: ...
    @comparison.setter
    def comparison(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]: ...
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): ...

class OrganizationConfigurationAutoEnableArgsDict(TypedDict):
    ec2: pulumi.Input[_builtins.bool]
    ecr: pulumi.Input[_builtins.bool]
    code_repository: NotRequired[pulumi.Input[_builtins.bool]]
    lambda_: NotRequired[pulumi.Input[_builtins.bool]]
    lambda_code: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class OrganizationConfigurationAutoEnableArgs:
    def __init__(
        __self__,
        *,
        ec2: pulumi.Input[_builtins.bool],
        ecr: pulumi.Input[_builtins.bool],
        code_repository: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_: Optional[pulumi.Input[_builtins.bool]] = ...,
        lambda_code: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def ec2(self) -> pulumi.Input[_builtins.bool]: ...
    @ec2.setter
    def ec2(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def ecr(self) -> pulumi.Input[_builtins.bool]: ...
    @ecr.setter
    def ecr(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="codeRepository")
    def code_repository(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @code_repository.setter
    def code_repository(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="lambdaCode")
    def lambda_code(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @lambda_code.setter
    def lambda_code(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
