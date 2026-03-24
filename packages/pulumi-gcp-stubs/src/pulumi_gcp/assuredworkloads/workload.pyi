import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["WorkloadArgs", "Workload"]

@pulumi.input_type
class WorkloadArgs:
    def __init__(
        __self__,
        *,
        compliance_regime: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        organization: pulumi.Input[_builtins.str],
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_sovereign_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_settings: Optional[pulumi.Input[WorkloadKmsSettingsArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        partner: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_permissions: Optional[
            pulumi.Input[WorkloadPartnerPermissionsArgs]
        ] = ...,
        partner_services_billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources_parent: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
        ] = ...,
        violation_notifications_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        workload_options: Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> pulumi.Input[_builtins.str]: ...
    @compliance_regime.setter
    def compliance_regime(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Input[_builtins.str]: ...
    @organization.setter
    def organization(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSovereignControls")
    def enable_sovereign_controls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sovereign_controls.setter
    def enable_sovereign_controls(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> Optional[pulumi.Input[WorkloadKmsSettingsArgs]]: ...
    @kms_settings.setter
    def kms_settings(self, value: Optional[pulumi.Input[WorkloadKmsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def partner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner.setter
    def partner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerPermissions")
    def partner_permissions(
        self,
    ) -> Optional[pulumi.Input[WorkloadPartnerPermissionsArgs]]: ...
    @partner_permissions.setter
    def partner_permissions(
        self, value: Optional[pulumi.Input[WorkloadPartnerPermissionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerServicesBillingAccount")
    def partner_services_billing_account(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_services_billing_account.setter
    def partner_services_billing_account(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioned_resources_parent.setter
    def provisioned_resources_parent(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
    ]: ...
    @resource_settings.setter
    def resource_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="violationNotificationsEnabled")
    def violation_notifications_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @violation_notifications_enabled.setter
    def violation_notifications_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadOptions")
    def workload_options(
        self,
    ) -> Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]]: ...
    @workload_options.setter
    def workload_options(
        self, value: Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]]
    ): ...

@pulumi.input_type
class _WorkloadState:
    def __init__(
        __self__,
        *,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_regime: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_statuses: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadComplianceStatusArgs]]]
        ] = ...,
        compliant_but_disallowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ekm_provisioning_responses: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadEkmProvisioningResponseArgs]]]
        ] = ...,
        enable_sovereign_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        kaj_enrollment_state: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_settings: Optional[pulumi.Input[WorkloadKmsSettingsArgs]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        partner: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_permissions: Optional[
            pulumi.Input[WorkloadPartnerPermissionsArgs]
        ] = ...,
        partner_services_billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources_parent: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
        ] = ...,
        resources: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadResourceArgs]]]
        ] = ...,
        saa_enrollment_responses: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadSaaEnrollmentResponseArgs]]]
        ] = ...,
        violation_notifications_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        workload_options: Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @billing_account.setter
    def billing_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compliance_regime.setter
    def compliance_regime(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkloadComplianceStatusArgs]]]
    ]: ...
    @compliance_statuses.setter
    def compliance_statuses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadComplianceStatusArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="compliantButDisallowedServices")
    def compliant_but_disallowed_services(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @compliant_but_disallowed_services.setter
    def compliant_but_disallowed_services(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @effective_labels.setter
    def effective_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningResponses")
    def ekm_provisioning_responses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkloadEkmProvisioningResponseArgs]]]
    ]: ...
    @ekm_provisioning_responses.setter
    def ekm_provisioning_responses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadEkmProvisioningResponseArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSovereignControls")
    def enable_sovereign_controls(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_sovereign_controls.setter
    def enable_sovereign_controls(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="kajEnrollmentState")
    def kaj_enrollment_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @kaj_enrollment_state.setter
    def kaj_enrollment_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> Optional[pulumi.Input[WorkloadKmsSettingsArgs]]: ...
    @kms_settings.setter
    def kms_settings(self, value: Optional[pulumi.Input[WorkloadKmsSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @organization.setter
    def organization(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def partner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner.setter
    def partner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="partnerPermissions")
    def partner_permissions(
        self,
    ) -> Optional[pulumi.Input[WorkloadPartnerPermissionsArgs]]: ...
    @partner_permissions.setter
    def partner_permissions(
        self, value: Optional[pulumi.Input[WorkloadPartnerPermissionsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="partnerServicesBillingAccount")
    def partner_services_billing_account(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @partner_services_billing_account.setter
    def partner_services_billing_account(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioned_resources_parent.setter
    def provisioned_resources_parent(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @pulumi_labels.setter
    def pulumi_labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
    ]: ...
    @resource_settings.setter
    def resource_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadResourceSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadResourceArgs]]]]: ...
    @resources.setter
    def resources(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[WorkloadResourceArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="saaEnrollmentResponses")
    def saa_enrollment_responses(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkloadSaaEnrollmentResponseArgs]]]
    ]: ...
    @saa_enrollment_responses.setter
    def saa_enrollment_responses(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkloadSaaEnrollmentResponseArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="violationNotificationsEnabled")
    def violation_notifications_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @violation_notifications_enabled.setter
    def violation_notifications_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="workloadOptions")
    def workload_options(
        self,
    ) -> Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]]: ...
    @workload_options.setter
    def workload_options(
        self, value: Optional[pulumi.Input[WorkloadWorkloadOptionsArgs]]
    ): ...

@pulumi.type_token("gcp:assuredworkloads/workload:Workload")
class Workload(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_regime: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_sovereign_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        kms_settings: Optional[
            pulumi.Input[Union[WorkloadKmsSettingsArgs, WorkloadKmsSettingsArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        partner: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_permissions: Optional[
            pulumi.Input[
                Union[
                    WorkloadPartnerPermissionsArgs, WorkloadPartnerPermissionsArgsDict
                ]
            ]
        ] = ...,
        partner_services_billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources_parent: Optional[pulumi.Input[_builtins.str]] = ...,
        resource_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadResourceSettingArgs, WorkloadResourceSettingArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        violation_notifications_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        workload_options: Optional[
            pulumi.Input[
                Union[WorkloadWorkloadOptionsArgs, WorkloadWorkloadOptionsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: WorkloadArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_regime: Optional[pulumi.Input[_builtins.str]] = ...,
        compliance_statuses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadComplianceStatusArgs,
                            WorkloadComplianceStatusArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        compliant_but_disallowed_services: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        ekm_provisioning_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadEkmProvisioningResponseArgs,
                            WorkloadEkmProvisioningResponseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        enable_sovereign_controls: Optional[pulumi.Input[_builtins.bool]] = ...,
        kaj_enrollment_state: Optional[pulumi.Input[_builtins.str]] = ...,
        kms_settings: Optional[
            pulumi.Input[Union[WorkloadKmsSettingsArgs, WorkloadKmsSettingsArgsDict]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        organization: Optional[pulumi.Input[_builtins.str]] = ...,
        partner: Optional[pulumi.Input[_builtins.str]] = ...,
        partner_permissions: Optional[
            pulumi.Input[
                Union[
                    WorkloadPartnerPermissionsArgs, WorkloadPartnerPermissionsArgsDict
                ]
            ]
        ] = ...,
        partner_services_billing_account: Optional[pulumi.Input[_builtins.str]] = ...,
        provisioned_resources_parent: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        resource_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadResourceSettingArgs, WorkloadResourceSettingArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        resources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[Union[WorkloadResourceArgs, WorkloadResourceArgsDict]]
                ]
            ]
        ] = ...,
        saa_enrollment_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            WorkloadSaaEnrollmentResponseArgs,
                            WorkloadSaaEnrollmentResponseArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        violation_notifications_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        workload_options: Optional[
            pulumi.Input[
                Union[WorkloadWorkloadOptionsArgs, WorkloadWorkloadOptionsArgsDict]
            ]
        ] = ...,
    ) -> Workload: ...
    @_builtins.property
    @pulumi.getter(name="billingAccount")
    def billing_account(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="complianceRegime")
    def compliance_regime(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="complianceStatuses")
    def compliance_statuses(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkloadComplianceStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="compliantButDisallowedServices")
    def compliant_but_disallowed_services(
        self,
    ) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="ekmProvisioningResponses")
    def ekm_provisioning_responses(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkloadEkmProvisioningResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="enableSovereignControls")
    def enable_sovereign_controls(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="kajEnrollmentState")
    def kaj_enrollment_state(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="kmsSettings")
    def kms_settings(self) -> pulumi.Output[Optional[outputs.WorkloadKmsSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def organization(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def partner(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="partnerPermissions")
    def partner_permissions(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkloadPartnerPermissions]]: ...
    @_builtins.property
    @pulumi.getter(name="partnerServicesBillingAccount")
    def partner_services_billing_account(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="provisionedResourcesParent")
    def provisioned_resources_parent(
        self,
    ) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="resourceSettings")
    def resource_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.WorkloadResourceSetting]]]: ...
    @_builtins.property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence[outputs.WorkloadResource]]: ...
    @_builtins.property
    @pulumi.getter(name="saaEnrollmentResponses")
    def saa_enrollment_responses(
        self,
    ) -> pulumi.Output[Sequence[outputs.WorkloadSaaEnrollmentResponse]]: ...
    @_builtins.property
    @pulumi.getter(name="violationNotificationsEnabled")
    def violation_notifications_enabled(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="workloadOptions")
    def workload_options(
        self,
    ) -> pulumi.Output[Optional[outputs.WorkloadWorkloadOptions]]: ...
