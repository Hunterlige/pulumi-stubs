

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ProviderArgs', 'Provider']
@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *, access_approval_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., access_context_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., access_token: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., add_pulumi_attribution_label: Optional[pulumi.Input[_builtins.bool]] = ..., alloydb_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., api_gateway_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apigee_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apihub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apikeys_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., app_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apphub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., artifact_registry_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., assured_workloads_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., backup_dr_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., batching: Optional[pulumi.Input[ProviderBatchingArgs]] = ..., beyondcorp_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., big_query_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., biglake_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., biglake_iceberg_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_analytics_hub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_connection_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_data_transfer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_datapolicy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_datapolicyv2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_reservation_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigtable_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., billing_project: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., blockchain_node_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., certificate_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., ces_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., chronicle_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_asset_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_build_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_functions_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_identity_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_ids_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_quotas_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_resource_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_run_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_run_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_scheduler_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_security_compliance_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_tasks_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloudbuildv2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., clouddeploy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., clouddomains_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloudfunctions2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., colab_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., composer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., compute_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., contact_center_insights_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_analysis_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_attached_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_aws_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_azure_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., core_billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[_builtins.str]] = ..., data_catalog_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_fusion_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_loss_prevention_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_pipeline_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., database_migration_service_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataflow_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataform_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_gdc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_metastore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., datastream_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., default_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., deployment_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., developer_connect_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dialogflow_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dialogflow_cx_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., disable_google_partner_name: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dns_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., document_ai_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., document_ai_warehouse_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., edgecontainer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., edgenetwork_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., essential_contacts_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., eventarc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., external_credentials: Optional[pulumi.Input[ProviderExternalCredentialsArgs]] = ..., filestore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_ai_logic_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_app_check_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_app_hosting_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_data_connect_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_database_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_extensions_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_hosting_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_storage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebaserules_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firestore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gemini_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_backup_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_hub2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_hub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gkeonprem_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., google_partner_name: Optional[pulumi.Input[_builtins.str]] = ..., healthcare_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., hypercomputecluster_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_beta_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_credentials_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_workforce_pool_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iap_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., identity_platform_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., impersonate_service_account: Optional[pulumi.Input[_builtins.str]] = ..., impersonate_service_account_delegates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., integration_connectors_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., integrations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., kms_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., logging_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., looker_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., lustre_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., managed_kafka_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., memcache_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., memorystore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., migration_center_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., ml_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., model_armor_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., model_armor_global_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., netapp_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_connectivity_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_connectivityv1_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_security_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_services_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., notebooks_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., observability_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., oracle_database_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., org_policy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_config_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_config_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_login_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parallelstore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parameter_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parameter_manager_regional_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., poll_interval: Optional[pulumi.Input[_builtins.str]] = ..., privateca_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., privileged_access_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., public_ca_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_lite_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_attribution_label_addition_strategy: Optional[pulumi.Input[_builtins.str]] = ..., recaptcha_enterprise_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., redis_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_reason: Optional[pulumi.Input[_builtins.str]] = ..., request_timeout: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager_v3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., runtime_config_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., runtimeconfig_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., saas_runtime_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., secret_manager_regional_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., secure_source_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_scanner_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., securityposture_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_directory_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_networking_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_usage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., site_verification_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., source_repo_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., spanner_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., sql_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_batch_operations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_control_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_insights_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_transfer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tags_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tags_location_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tpu_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., transcoder_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., universe_domain: Optional[pulumi.Input[_builtins.str]] = ..., user_project_override: Optional[pulumi.Input[_builtins.bool]] = ..., vector_search_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vertex_ai_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vmwareengine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workbench_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workflows_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workstations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessApprovalCustomEndpoint")
    def access_approval_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_approval_custom_endpoint.setter
    def access_approval_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessContextManagerCustomEndpoint")
    def access_context_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_context_manager_custom_endpoint.setter
    def access_context_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryCustomEndpoint")
    def active_directory_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @active_directory_custom_endpoint.setter
    def active_directory_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="addPulumiAttributionLabel")
    def add_pulumi_attribution_label(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @add_pulumi_attribution_label.setter
    def add_pulumi_attribution_label(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alloydbCustomEndpoint")
    def alloydb_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @alloydb_custom_endpoint.setter
    def alloydb_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiGatewayCustomEndpoint")
    def api_gateway_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @api_gateway_custom_endpoint.setter
    def api_gateway_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apigeeCustomEndpoint")
    def apigee_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @apigee_custom_endpoint.setter
    def apigee_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apihubCustomEndpoint")
    def apihub_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @apihub_custom_endpoint.setter
    def apihub_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apikeysCustomEndpoint")
    def apikeys_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @apikeys_custom_endpoint.setter
    def apikeys_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineCustomEndpoint")
    def app_engine_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @app_engine_custom_endpoint.setter
    def app_engine_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apphubCustomEndpoint")
    def apphub_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @apphub_custom_endpoint.setter
    def apphub_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactRegistryCustomEndpoint")
    def artifact_registry_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @artifact_registry_custom_endpoint.setter
    def artifact_registry_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assuredWorkloadsCustomEndpoint")
    def assured_workloads_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @assured_workloads_custom_endpoint.setter
    def assured_workloads_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupDrCustomEndpoint")
    def backup_dr_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @backup_dr_custom_endpoint.setter
    def backup_dr_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def batching(self) -> Optional[pulumi.Input[ProviderBatchingArgs]]:
        ...
    
    @batching.setter
    def batching(self, value: Optional[pulumi.Input[ProviderBatchingArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beyondcorpCustomEndpoint")
    def beyondcorp_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @beyondcorp_custom_endpoint.setter
    def beyondcorp_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigQueryCustomEndpoint")
    def big_query_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @big_query_custom_endpoint.setter
    def big_query_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeCustomEndpoint")
    def biglake_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @biglake_custom_endpoint.setter
    def biglake_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeIcebergCustomEndpoint")
    def biglake_iceberg_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @biglake_iceberg_custom_endpoint.setter
    def biglake_iceberg_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryAnalyticsHubCustomEndpoint")
    def bigquery_analytics_hub_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_analytics_hub_custom_endpoint.setter
    def bigquery_analytics_hub_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryConnectionCustomEndpoint")
    def bigquery_connection_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_connection_custom_endpoint.setter
    def bigquery_connection_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDataTransferCustomEndpoint")
    def bigquery_data_transfer_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_data_transfer_custom_endpoint.setter
    def bigquery_data_transfer_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatapolicyCustomEndpoint")
    def bigquery_datapolicy_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_datapolicy_custom_endpoint.setter
    def bigquery_datapolicy_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatapolicyv2CustomEndpoint")
    def bigquery_datapolicyv2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_datapolicyv2_custom_endpoint.setter
    def bigquery_datapolicyv2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryReservationCustomEndpoint")
    def bigquery_reservation_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigquery_reservation_custom_endpoint.setter
    def bigquery_reservation_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigtableCustomEndpoint")
    def bigtable_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @bigtable_custom_endpoint.setter
    def bigtable_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingCustomEndpoint")
    def billing_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @billing_custom_endpoint.setter
    def billing_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProject")
    def billing_project(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @billing_project.setter
    def billing_project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationCustomEndpoint")
    def binary_authorization_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @binary_authorization_custom_endpoint.setter
    def binary_authorization_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainNodeEngineCustomEndpoint")
    def blockchain_node_engine_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @blockchain_node_engine_custom_endpoint.setter
    def blockchain_node_engine_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateManagerCustomEndpoint")
    def certificate_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @certificate_manager_custom_endpoint.setter
    def certificate_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cesCustomEndpoint")
    def ces_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @ces_custom_endpoint.setter
    def ces_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chronicleCustomEndpoint")
    def chronicle_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @chronicle_custom_endpoint.setter
    def chronicle_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudAssetCustomEndpoint")
    def cloud_asset_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_asset_custom_endpoint.setter
    def cloud_asset_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBillingCustomEndpoint")
    def cloud_billing_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_billing_custom_endpoint.setter
    def cloud_billing_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBuildCustomEndpoint")
    def cloud_build_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_build_custom_endpoint.setter
    def cloud_build_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFunctionsCustomEndpoint")
    def cloud_functions_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_functions_custom_endpoint.setter
    def cloud_functions_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIdentityCustomEndpoint")
    def cloud_identity_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_identity_custom_endpoint.setter
    def cloud_identity_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIdsCustomEndpoint")
    def cloud_ids_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_ids_custom_endpoint.setter
    def cloud_ids_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudQuotasCustomEndpoint")
    def cloud_quotas_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_quotas_custom_endpoint.setter
    def cloud_quotas_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudResourceManagerCustomEndpoint")
    def cloud_resource_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_resource_manager_custom_endpoint.setter
    def cloud_resource_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRunCustomEndpoint")
    def cloud_run_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_run_custom_endpoint.setter
    def cloud_run_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRunV2CustomEndpoint")
    def cloud_run_v2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_run_v2_custom_endpoint.setter
    def cloud_run_v2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSchedulerCustomEndpoint")
    def cloud_scheduler_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_scheduler_custom_endpoint.setter
    def cloud_scheduler_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSecurityComplianceCustomEndpoint")
    def cloud_security_compliance_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_security_compliance_custom_endpoint.setter
    def cloud_security_compliance_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudTasksCustomEndpoint")
    def cloud_tasks_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloud_tasks_custom_endpoint.setter
    def cloud_tasks_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudbuildv2CustomEndpoint")
    def cloudbuildv2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloudbuildv2_custom_endpoint.setter
    def cloudbuildv2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clouddeployCustomEndpoint")
    def clouddeploy_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @clouddeploy_custom_endpoint.setter
    def clouddeploy_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clouddomainsCustomEndpoint")
    def clouddomains_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @clouddomains_custom_endpoint.setter
    def clouddomains_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfunctions2CustomEndpoint")
    def cloudfunctions2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @cloudfunctions2_custom_endpoint.setter
    def cloudfunctions2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="colabCustomEndpoint")
    def colab_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @colab_custom_endpoint.setter
    def colab_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerCustomEndpoint")
    def composer_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @composer_custom_endpoint.setter
    def composer_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCustomEndpoint")
    def compute_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @compute_custom_endpoint.setter
    def compute_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactCenterInsightsCustomEndpoint")
    def contact_center_insights_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @contact_center_insights_custom_endpoint.setter
    def contact_center_insights_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAnalysisCustomEndpoint")
    def container_analysis_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @container_analysis_custom_endpoint.setter
    def container_analysis_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAttachedCustomEndpoint")
    def container_attached_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @container_attached_custom_endpoint.setter
    def container_attached_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAwsCustomEndpoint")
    def container_aws_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @container_aws_custom_endpoint.setter
    def container_aws_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAzureCustomEndpoint")
    def container_azure_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @container_azure_custom_endpoint.setter
    def container_azure_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerCustomEndpoint")
    def container_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @container_custom_endpoint.setter
    def container_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreBillingCustomEndpoint")
    def core_billing_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @core_billing_custom_endpoint.setter
    def core_billing_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogCustomEndpoint")
    def data_catalog_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_catalog_custom_endpoint.setter
    def data_catalog_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFusionCustomEndpoint")
    def data_fusion_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_fusion_custom_endpoint.setter
    def data_fusion_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLossPreventionCustomEndpoint")
    def data_loss_prevention_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_loss_prevention_custom_endpoint.setter
    def data_loss_prevention_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPipelineCustomEndpoint")
    def data_pipeline_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @data_pipeline_custom_endpoint.setter
    def data_pipeline_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseMigrationServiceCustomEndpoint")
    def database_migration_service_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @database_migration_service_custom_endpoint.setter
    def database_migration_service_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataflowCustomEndpoint")
    def dataflow_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataflow_custom_endpoint.setter
    def dataflow_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformCustomEndpoint")
    def dataform_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataform_custom_endpoint.setter
    def dataform_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexCustomEndpoint")
    def dataplex_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataplex_custom_endpoint.setter
    def dataplex_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocCustomEndpoint")
    def dataproc_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataproc_custom_endpoint.setter
    def dataproc_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocGdcCustomEndpoint")
    def dataproc_gdc_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataproc_gdc_custom_endpoint.setter
    def dataproc_gdc_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreCustomEndpoint")
    def dataproc_metastore_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dataproc_metastore_custom_endpoint.setter
    def dataproc_metastore_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastreamCustomEndpoint")
    def datastream_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @datastream_custom_endpoint.setter
    def datastream_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLabels")
    def default_labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        ...
    
    @default_labels.setter
    def default_labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentManagerCustomEndpoint")
    def deployment_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @deployment_manager_custom_endpoint.setter
    def deployment_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerConnectCustomEndpoint")
    def developer_connect_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @developer_connect_custom_endpoint.setter
    def developer_connect_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowCustomEndpoint")
    def dialogflow_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dialogflow_custom_endpoint.setter
    def dialogflow_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowCxCustomEndpoint")
    def dialogflow_cx_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dialogflow_cx_custom_endpoint.setter
    def dialogflow_cx_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableGooglePartnerName")
    def disable_google_partner_name(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @disable_google_partner_name.setter
    def disable_google_partner_name(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEngineCustomEndpoint")
    def discovery_engine_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @discovery_engine_custom_endpoint.setter
    def discovery_engine_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsCustomEndpoint")
    def dns_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @dns_custom_endpoint.setter
    def dns_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentAiCustomEndpoint")
    def document_ai_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @document_ai_custom_endpoint.setter
    def document_ai_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentAiWarehouseCustomEndpoint")
    def document_ai_warehouse_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @document_ai_warehouse_custom_endpoint.setter
    def document_ai_warehouse_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgecontainerCustomEndpoint")
    def edgecontainer_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @edgecontainer_custom_endpoint.setter
    def edgecontainer_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgenetworkCustomEndpoint")
    def edgenetwork_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @edgenetwork_custom_endpoint.setter
    def edgenetwork_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="essentialContactsCustomEndpoint")
    def essential_contacts_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @essential_contacts_custom_endpoint.setter
    def essential_contacts_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventarcCustomEndpoint")
    def eventarc_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @eventarc_custom_endpoint.setter
    def eventarc_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalCredentials")
    def external_credentials(self) -> Optional[pulumi.Input[ProviderExternalCredentialsArgs]]:
        ...
    
    @external_credentials.setter
    def external_credentials(self, value: Optional[pulumi.Input[ProviderExternalCredentialsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filestoreCustomEndpoint")
    def filestore_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @filestore_custom_endpoint.setter
    def filestore_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAiLogicCustomEndpoint")
    def firebase_ai_logic_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_ai_logic_custom_endpoint.setter
    def firebase_ai_logic_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAppCheckCustomEndpoint")
    def firebase_app_check_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_app_check_custom_endpoint.setter
    def firebase_app_check_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAppHostingCustomEndpoint")
    def firebase_app_hosting_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_app_hosting_custom_endpoint.setter
    def firebase_app_hosting_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseCustomEndpoint")
    def firebase_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_custom_endpoint.setter
    def firebase_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseDataConnectCustomEndpoint")
    def firebase_data_connect_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_data_connect_custom_endpoint.setter
    def firebase_data_connect_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseDatabaseCustomEndpoint")
    def firebase_database_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_database_custom_endpoint.setter
    def firebase_database_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseExtensionsCustomEndpoint")
    def firebase_extensions_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_extensions_custom_endpoint.setter
    def firebase_extensions_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseHostingCustomEndpoint")
    def firebase_hosting_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_hosting_custom_endpoint.setter
    def firebase_hosting_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseStorageCustomEndpoint")
    def firebase_storage_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebase_storage_custom_endpoint.setter
    def firebase_storage_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaserulesCustomEndpoint")
    def firebaserules_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firebaserules_custom_endpoint.setter
    def firebaserules_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firestoreCustomEndpoint")
    def firestore_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @firestore_custom_endpoint.setter
    def firestore_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geminiCustomEndpoint")
    def gemini_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gemini_custom_endpoint.setter
    def gemini_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeBackupCustomEndpoint")
    def gke_backup_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gke_backup_custom_endpoint.setter
    def gke_backup_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeHub2CustomEndpoint")
    def gke_hub2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gke_hub2_custom_endpoint.setter
    def gke_hub2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeHubCustomEndpoint")
    def gke_hub_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gke_hub_custom_endpoint.setter
    def gke_hub_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeonpremCustomEndpoint")
    def gkeonprem_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @gkeonprem_custom_endpoint.setter
    def gkeonprem_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googlePartnerName")
    def google_partner_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @google_partner_name.setter
    def google_partner_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthcareCustomEndpoint")
    def healthcare_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @healthcare_custom_endpoint.setter
    def healthcare_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hypercomputeclusterCustomEndpoint")
    def hypercomputecluster_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @hypercomputecluster_custom_endpoint.setter
    def hypercomputecluster_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iam2CustomEndpoint")
    def iam2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam2_custom_endpoint.setter
    def iam2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iam3CustomEndpoint")
    def iam3_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam3_custom_endpoint.setter
    def iam3_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamBetaCustomEndpoint")
    def iam_beta_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_beta_custom_endpoint.setter
    def iam_beta_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamCredentialsCustomEndpoint")
    def iam_credentials_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_credentials_custom_endpoint.setter
    def iam_credentials_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamCustomEndpoint")
    def iam_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_custom_endpoint.setter
    def iam_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamWorkforcePoolCustomEndpoint")
    def iam_workforce_pool_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iam_workforce_pool_custom_endpoint.setter
    def iam_workforce_pool_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iapCustomEndpoint")
    def iap_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @iap_custom_endpoint.setter
    def iap_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPlatformCustomEndpoint")
    def identity_platform_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @identity_platform_custom_endpoint.setter
    def identity_platform_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impersonateServiceAccount")
    def impersonate_service_account(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @impersonate_service_account.setter
    def impersonate_service_account(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impersonateServiceAccountDelegates")
    def impersonate_service_account_delegates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @impersonate_service_account_delegates.setter
    def impersonate_service_account_delegates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationConnectorsCustomEndpoint")
    def integration_connectors_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @integration_connectors_custom_endpoint.setter
    def integration_connectors_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationsCustomEndpoint")
    def integrations_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @integrations_custom_endpoint.setter
    def integrations_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsCustomEndpoint")
    def kms_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @kms_custom_endpoint.setter
    def kms_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingCustomEndpoint")
    def logging_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @logging_custom_endpoint.setter
    def logging_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookerCustomEndpoint")
    def looker_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @looker_custom_endpoint.setter
    def looker_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lustreCustomEndpoint")
    def lustre_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @lustre_custom_endpoint.setter
    def lustre_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedKafkaCustomEndpoint")
    def managed_kafka_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @managed_kafka_custom_endpoint.setter
    def managed_kafka_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheCustomEndpoint")
    def memcache_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @memcache_custom_endpoint.setter
    def memcache_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorystoreCustomEndpoint")
    def memorystore_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @memorystore_custom_endpoint.setter
    def memorystore_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationCenterCustomEndpoint")
    def migration_center_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @migration_center_custom_endpoint.setter
    def migration_center_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlEngineCustomEndpoint")
    def ml_engine_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @ml_engine_custom_endpoint.setter
    def ml_engine_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelArmorCustomEndpoint")
    def model_armor_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @model_armor_custom_endpoint.setter
    def model_armor_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelArmorGlobalCustomEndpoint")
    def model_armor_global_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @model_armor_global_custom_endpoint.setter
    def model_armor_global_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringCustomEndpoint")
    def monitoring_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @monitoring_custom_endpoint.setter
    def monitoring_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="netappCustomEndpoint")
    def netapp_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @netapp_custom_endpoint.setter
    def netapp_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConnectivityCustomEndpoint")
    def network_connectivity_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_connectivity_custom_endpoint.setter
    def network_connectivity_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConnectivityv1CustomEndpoint")
    def network_connectivityv1_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_connectivityv1_custom_endpoint.setter
    def network_connectivityv1_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkManagementCustomEndpoint")
    def network_management_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_management_custom_endpoint.setter
    def network_management_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityCustomEndpoint")
    def network_security_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_security_custom_endpoint.setter
    def network_security_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkServicesCustomEndpoint")
    def network_services_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @network_services_custom_endpoint.setter
    def network_services_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebooksCustomEndpoint")
    def notebooks_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @notebooks_custom_endpoint.setter
    def notebooks_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityCustomEndpoint")
    def observability_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @observability_custom_endpoint.setter
    def observability_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oracleDatabaseCustomEndpoint")
    def oracle_database_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @oracle_database_custom_endpoint.setter
    def oracle_database_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgPolicyCustomEndpoint")
    def org_policy_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @org_policy_custom_endpoint.setter
    def org_policy_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osConfigCustomEndpoint")
    def os_config_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @os_config_custom_endpoint.setter
    def os_config_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osConfigV2CustomEndpoint")
    def os_config_v2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @os_config_v2_custom_endpoint.setter
    def os_config_v2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osLoginCustomEndpoint")
    def os_login_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @os_login_custom_endpoint.setter
    def os_login_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelstoreCustomEndpoint")
    def parallelstore_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @parallelstore_custom_endpoint.setter
    def parallelstore_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterManagerCustomEndpoint")
    def parameter_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @parameter_manager_custom_endpoint.setter
    def parameter_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterManagerRegionalCustomEndpoint")
    def parameter_manager_regional_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @parameter_manager_regional_custom_endpoint.setter
    def parameter_manager_regional_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollInterval")
    def poll_interval(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @poll_interval.setter
    def poll_interval(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privatecaCustomEndpoint")
    def privateca_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @privateca_custom_endpoint.setter
    def privateca_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegedAccessManagerCustomEndpoint")
    def privileged_access_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @privileged_access_manager_custom_endpoint.setter
    def privileged_access_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicCaCustomEndpoint")
    def public_ca_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @public_ca_custom_endpoint.setter
    def public_ca_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubCustomEndpoint")
    def pubsub_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @pubsub_custom_endpoint.setter
    def pubsub_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubLiteCustomEndpoint")
    def pubsub_lite_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @pubsub_lite_custom_endpoint.setter
    def pubsub_lite_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiAttributionLabelAdditionStrategy")
    def pulumi_attribution_label_addition_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @pulumi_attribution_label_addition_strategy.setter
    def pulumi_attribution_label_addition_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recaptchaEnterpriseCustomEndpoint")
    def recaptcha_enterprise_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @recaptcha_enterprise_custom_endpoint.setter
    def recaptcha_enterprise_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisCustomEndpoint")
    def redis_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @redis_custom_endpoint.setter
    def redis_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestReason")
    def request_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @request_reason.setter
    def request_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTimeout")
    def request_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @request_timeout.setter
    def request_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManager3CustomEndpoint")
    def resource_manager3_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_manager3_custom_endpoint.setter
    def resource_manager3_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerCustomEndpoint")
    def resource_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_manager_custom_endpoint.setter
    def resource_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerV3CustomEndpoint")
    def resource_manager_v3_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @resource_manager_v3_custom_endpoint.setter
    def resource_manager_v3_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeConfigCustomEndpoint")
    def runtime_config_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @runtime_config_custom_endpoint.setter
    def runtime_config_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeconfigCustomEndpoint")
    def runtimeconfig_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @runtimeconfig_custom_endpoint.setter
    def runtimeconfig_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saasRuntimeCustomEndpoint")
    def saas_runtime_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @saas_runtime_custom_endpoint.setter
    def saas_runtime_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerCustomEndpoint")
    def secret_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secret_manager_custom_endpoint.setter
    def secret_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerRegionalCustomEndpoint")
    def secret_manager_regional_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secret_manager_regional_custom_endpoint.setter
    def secret_manager_regional_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureSourceManagerCustomEndpoint")
    def secure_source_manager_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @secure_source_manager_custom_endpoint.setter
    def secure_source_manager_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterCustomEndpoint")
    def security_center_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_center_custom_endpoint.setter
    def security_center_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterManagementCustomEndpoint")
    def security_center_management_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_center_management_custom_endpoint.setter
    def security_center_management_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterV2CustomEndpoint")
    def security_center_v2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_center_v2_custom_endpoint.setter
    def security_center_v2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityScannerCustomEndpoint")
    def security_scanner_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @security_scanner_custom_endpoint.setter
    def security_scanner_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitypostureCustomEndpoint")
    def securityposture_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @securityposture_custom_endpoint.setter
    def securityposture_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryCustomEndpoint")
    def service_directory_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @service_directory_custom_endpoint.setter
    def service_directory_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceManagementCustomEndpoint")
    def service_management_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @service_management_custom_endpoint.setter
    def service_management_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkingCustomEndpoint")
    def service_networking_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @service_networking_custom_endpoint.setter
    def service_networking_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUsageCustomEndpoint")
    def service_usage_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @service_usage_custom_endpoint.setter
    def service_usage_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteVerificationCustomEndpoint")
    def site_verification_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @site_verification_custom_endpoint.setter
    def site_verification_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRepoCustomEndpoint")
    def source_repo_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @source_repo_custom_endpoint.setter
    def source_repo_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spannerCustomEndpoint")
    def spanner_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @spanner_custom_endpoint.setter
    def spanner_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlCustomEndpoint")
    def sql_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @sql_custom_endpoint.setter
    def sql_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageBatchOperationsCustomEndpoint")
    def storage_batch_operations_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @storage_batch_operations_custom_endpoint.setter
    def storage_batch_operations_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageControlCustomEndpoint")
    def storage_control_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @storage_control_custom_endpoint.setter
    def storage_control_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCustomEndpoint")
    def storage_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @storage_custom_endpoint.setter
    def storage_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageInsightsCustomEndpoint")
    def storage_insights_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @storage_insights_custom_endpoint.setter
    def storage_insights_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTransferCustomEndpoint")
    def storage_transfer_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @storage_transfer_custom_endpoint.setter
    def storage_transfer_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsCustomEndpoint")
    def tags_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @tags_custom_endpoint.setter
    def tags_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsLocationCustomEndpoint")
    def tags_location_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @tags_location_custom_endpoint.setter
    def tags_location_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuV2CustomEndpoint")
    def tpu_v2_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @tpu_v2_custom_endpoint.setter
    def tpu_v2_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transcoderCustomEndpoint")
    def transcoder_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @transcoder_custom_endpoint.setter
    def transcoder_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="universeDomain")
    def universe_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @universe_domain.setter
    def universe_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="userProjectOverride")
    def user_project_override(self) -> Optional[pulumi.Input[_builtins.bool]]:
        ...
    
    @user_project_override.setter
    def user_project_override(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorSearchCustomEndpoint")
    def vector_search_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vector_search_custom_endpoint.setter
    def vector_search_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vertexAiCustomEndpoint")
    def vertex_ai_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vertex_ai_custom_endpoint.setter
    def vertex_ai_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareengineCustomEndpoint")
    def vmwareengine_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vmwareengine_custom_endpoint.setter
    def vmwareengine_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccessCustomEndpoint")
    def vpc_access_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @vpc_access_custom_endpoint.setter
    def vpc_access_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workbenchCustomEndpoint")
    def workbench_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @workbench_custom_endpoint.setter
    def workbench_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowsCustomEndpoint")
    def workflows_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @workflows_custom_endpoint.setter
    def workflows_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workstationsCustomEndpoint")
    def workstations_custom_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @workstations_custom_endpoint.setter
    def workstations_custom_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @zone.setter
    def zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("pulumi:providers:gcp")
class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_approval_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., access_context_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., access_token: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., add_pulumi_attribution_label: Optional[pulumi.Input[_builtins.bool]] = ..., alloydb_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., api_gateway_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apigee_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apihub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apikeys_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., app_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., apphub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., artifact_registry_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., assured_workloads_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., backup_dr_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., batching: Optional[pulumi.Input[Union[ProviderBatchingArgs, ProviderBatchingArgsDict]]] = ..., beyondcorp_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., big_query_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., biglake_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., biglake_iceberg_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_analytics_hub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_connection_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_data_transfer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_datapolicy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_datapolicyv2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigquery_reservation_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., bigtable_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., billing_project: Optional[pulumi.Input[_builtins.str]] = ..., binary_authorization_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., blockchain_node_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., certificate_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., ces_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., chronicle_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_asset_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_build_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_functions_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_identity_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_ids_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_quotas_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_resource_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_run_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_run_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_scheduler_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_security_compliance_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloud_tasks_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloudbuildv2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., clouddeploy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., clouddomains_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., cloudfunctions2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., colab_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., composer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., compute_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., contact_center_insights_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_analysis_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_attached_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_aws_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_azure_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., container_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., core_billing_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., credentials: Optional[pulumi.Input[_builtins.str]] = ..., data_catalog_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_fusion_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_loss_prevention_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., data_pipeline_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., database_migration_service_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataflow_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataform_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataplex_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_gdc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dataproc_metastore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., datastream_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., default_labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., deployment_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., developer_connect_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dialogflow_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dialogflow_cx_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., disable_google_partner_name: Optional[pulumi.Input[_builtins.bool]] = ..., discovery_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., dns_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., document_ai_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., document_ai_warehouse_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., edgecontainer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., edgenetwork_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., essential_contacts_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., eventarc_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., external_credentials: Optional[pulumi.Input[Union[ProviderExternalCredentialsArgs, ProviderExternalCredentialsArgsDict]]] = ..., filestore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_ai_logic_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_app_check_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_app_hosting_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_data_connect_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_database_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_extensions_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_hosting_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebase_storage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firebaserules_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., firestore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gemini_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_backup_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_hub2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gke_hub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., gkeonprem_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., google_partner_name: Optional[pulumi.Input[_builtins.str]] = ..., healthcare_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., hypercomputecluster_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_beta_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_credentials_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iam_workforce_pool_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., iap_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., identity_platform_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., impersonate_service_account: Optional[pulumi.Input[_builtins.str]] = ..., impersonate_service_account_delegates: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., integration_connectors_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., integrations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., kms_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., logging_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., looker_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., lustre_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., managed_kafka_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., memcache_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., memorystore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., migration_center_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., ml_engine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., model_armor_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., model_armor_global_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., monitoring_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., netapp_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_connectivity_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_connectivityv1_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_security_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., network_services_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., notebooks_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., observability_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., oracle_database_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., org_policy_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_config_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_config_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., os_login_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parallelstore_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parameter_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., parameter_manager_regional_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., poll_interval: Optional[pulumi.Input[_builtins.str]] = ..., privateca_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., privileged_access_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., public_ca_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pubsub_lite_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., pulumi_attribution_label_addition_strategy: Optional[pulumi.Input[_builtins.str]] = ..., recaptcha_enterprise_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., redis_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., request_reason: Optional[pulumi.Input[_builtins.str]] = ..., request_timeout: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., resource_manager_v3_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., runtime_config_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., runtimeconfig_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., saas_runtime_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., secret_manager_regional_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., secure_source_manager_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_center_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., security_scanner_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., securityposture_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_directory_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_management_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_networking_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., service_usage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., site_verification_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., source_repo_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., spanner_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., sql_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_batch_operations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_control_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_insights_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., storage_transfer_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tags_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tags_location_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., tpu_v2_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., transcoder_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., universe_domain: Optional[pulumi.Input[_builtins.str]] = ..., user_project_override: Optional[pulumi.Input[_builtins.bool]] = ..., vector_search_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vertex_ai_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vmwareengine_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., vpc_access_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workbench_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workflows_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., workstations_custom_endpoint: Optional[pulumi.Input[_builtins.str]] = ..., zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[ProviderArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessApprovalCustomEndpoint")
    def access_approval_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessContextManagerCustomEndpoint")
    def access_context_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryCustomEndpoint")
    def active_directory_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="alloydbCustomEndpoint")
    def alloydb_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiGatewayCustomEndpoint")
    def api_gateway_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apigeeCustomEndpoint")
    def apigee_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apihubCustomEndpoint")
    def apihub_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apikeysCustomEndpoint")
    def apikeys_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="appEngineCustomEndpoint")
    def app_engine_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apphubCustomEndpoint")
    def apphub_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="artifactRegistryCustomEndpoint")
    def artifact_registry_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="assuredWorkloadsCustomEndpoint")
    def assured_workloads_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="backupDrCustomEndpoint")
    def backup_dr_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beyondcorpCustomEndpoint")
    def beyondcorp_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigQueryCustomEndpoint")
    def big_query_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeCustomEndpoint")
    def biglake_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="biglakeIcebergCustomEndpoint")
    def biglake_iceberg_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryAnalyticsHubCustomEndpoint")
    def bigquery_analytics_hub_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryConnectionCustomEndpoint")
    def bigquery_connection_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDataTransferCustomEndpoint")
    def bigquery_data_transfer_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatapolicyCustomEndpoint")
    def bigquery_datapolicy_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryDatapolicyv2CustomEndpoint")
    def bigquery_datapolicyv2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryReservationCustomEndpoint")
    def bigquery_reservation_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigtableCustomEndpoint")
    def bigtable_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingCustomEndpoint")
    def billing_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="billingProject")
    def billing_project(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="binaryAuthorizationCustomEndpoint")
    def binary_authorization_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="blockchainNodeEngineCustomEndpoint")
    def blockchain_node_engine_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="certificateManagerCustomEndpoint")
    def certificate_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cesCustomEndpoint")
    def ces_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="chronicleCustomEndpoint")
    def chronicle_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudAssetCustomEndpoint")
    def cloud_asset_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBillingCustomEndpoint")
    def cloud_billing_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudBuildCustomEndpoint")
    def cloud_build_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudFunctionsCustomEndpoint")
    def cloud_functions_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIdentityCustomEndpoint")
    def cloud_identity_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudIdsCustomEndpoint")
    def cloud_ids_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudQuotasCustomEndpoint")
    def cloud_quotas_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudResourceManagerCustomEndpoint")
    def cloud_resource_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRunCustomEndpoint")
    def cloud_run_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudRunV2CustomEndpoint")
    def cloud_run_v2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSchedulerCustomEndpoint")
    def cloud_scheduler_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudSecurityComplianceCustomEndpoint")
    def cloud_security_compliance_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudTasksCustomEndpoint")
    def cloud_tasks_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudbuildv2CustomEndpoint")
    def cloudbuildv2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clouddeployCustomEndpoint")
    def clouddeploy_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clouddomainsCustomEndpoint")
    def clouddomains_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudfunctions2CustomEndpoint")
    def cloudfunctions2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="colabCustomEndpoint")
    def colab_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="composerCustomEndpoint")
    def composer_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeCustomEndpoint")
    def compute_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactCenterInsightsCustomEndpoint")
    def contact_center_insights_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAnalysisCustomEndpoint")
    def container_analysis_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAttachedCustomEndpoint")
    def container_attached_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAwsCustomEndpoint")
    def container_aws_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerAzureCustomEndpoint")
    def container_azure_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="containerCustomEndpoint")
    def container_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="coreBillingCustomEndpoint")
    def core_billing_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataCatalogCustomEndpoint")
    def data_catalog_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataFusionCustomEndpoint")
    def data_fusion_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataLossPreventionCustomEndpoint")
    def data_loss_prevention_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataPipelineCustomEndpoint")
    def data_pipeline_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="databaseMigrationServiceCustomEndpoint")
    def database_migration_service_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataflowCustomEndpoint")
    def dataflow_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataformCustomEndpoint")
    def dataform_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataplexCustomEndpoint")
    def dataplex_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocCustomEndpoint")
    def dataproc_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocGdcCustomEndpoint")
    def dataproc_gdc_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataprocMetastoreCustomEndpoint")
    def dataproc_metastore_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datastreamCustomEndpoint")
    def datastream_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentManagerCustomEndpoint")
    def deployment_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="developerConnectCustomEndpoint")
    def developer_connect_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowCustomEndpoint")
    def dialogflow_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowCxCustomEndpoint")
    def dialogflow_cx_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="discoveryEngineCustomEndpoint")
    def discovery_engine_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dnsCustomEndpoint")
    def dns_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentAiCustomEndpoint")
    def document_ai_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentAiWarehouseCustomEndpoint")
    def document_ai_warehouse_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgecontainerCustomEndpoint")
    def edgecontainer_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="edgenetworkCustomEndpoint")
    def edgenetwork_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="essentialContactsCustomEndpoint")
    def essential_contacts_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventarcCustomEndpoint")
    def eventarc_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="filestoreCustomEndpoint")
    def filestore_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAiLogicCustomEndpoint")
    def firebase_ai_logic_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAppCheckCustomEndpoint")
    def firebase_app_check_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseAppHostingCustomEndpoint")
    def firebase_app_hosting_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseCustomEndpoint")
    def firebase_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseDataConnectCustomEndpoint")
    def firebase_data_connect_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseDatabaseCustomEndpoint")
    def firebase_database_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseExtensionsCustomEndpoint")
    def firebase_extensions_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseHostingCustomEndpoint")
    def firebase_hosting_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaseStorageCustomEndpoint")
    def firebase_storage_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firebaserulesCustomEndpoint")
    def firebaserules_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firestoreCustomEndpoint")
    def firestore_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="geminiCustomEndpoint")
    def gemini_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeBackupCustomEndpoint")
    def gke_backup_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeHub2CustomEndpoint")
    def gke_hub2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeHubCustomEndpoint")
    def gke_hub_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gkeonpremCustomEndpoint")
    def gkeonprem_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="googlePartnerName")
    def google_partner_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="healthcareCustomEndpoint")
    def healthcare_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="hypercomputeclusterCustomEndpoint")
    def hypercomputecluster_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iam2CustomEndpoint")
    def iam2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iam3CustomEndpoint")
    def iam3_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamBetaCustomEndpoint")
    def iam_beta_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamCredentialsCustomEndpoint")
    def iam_credentials_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamCustomEndpoint")
    def iam_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamWorkforcePoolCustomEndpoint")
    def iam_workforce_pool_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iapCustomEndpoint")
    def iap_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="identityPlatformCustomEndpoint")
    def identity_platform_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="impersonateServiceAccount")
    def impersonate_service_account(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationConnectorsCustomEndpoint")
    def integration_connectors_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="integrationsCustomEndpoint")
    def integrations_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsCustomEndpoint")
    def kms_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingCustomEndpoint")
    def logging_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lookerCustomEndpoint")
    def looker_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lustreCustomEndpoint")
    def lustre_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="managedKafkaCustomEndpoint")
    def managed_kafka_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memcacheCustomEndpoint")
    def memcache_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memorystoreCustomEndpoint")
    def memorystore_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="migrationCenterCustomEndpoint")
    def migration_center_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mlEngineCustomEndpoint")
    def ml_engine_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelArmorCustomEndpoint")
    def model_armor_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelArmorGlobalCustomEndpoint")
    def model_armor_global_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="monitoringCustomEndpoint")
    def monitoring_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="netappCustomEndpoint")
    def netapp_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConnectivityCustomEndpoint")
    def network_connectivity_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkConnectivityv1CustomEndpoint")
    def network_connectivityv1_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkManagementCustomEndpoint")
    def network_management_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkSecurityCustomEndpoint")
    def network_security_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="networkServicesCustomEndpoint")
    def network_services_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notebooksCustomEndpoint")
    def notebooks_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="observabilityCustomEndpoint")
    def observability_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oracleDatabaseCustomEndpoint")
    def oracle_database_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="orgPolicyCustomEndpoint")
    def org_policy_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osConfigCustomEndpoint")
    def os_config_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osConfigV2CustomEndpoint")
    def os_config_v2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="osLoginCustomEndpoint")
    def os_login_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parallelstoreCustomEndpoint")
    def parallelstore_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterManagerCustomEndpoint")
    def parameter_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterManagerRegionalCustomEndpoint")
    def parameter_manager_regional_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pollInterval")
    def poll_interval(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privatecaCustomEndpoint")
    def privateca_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="privilegedAccessManagerCustomEndpoint")
    def privileged_access_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="publicCaCustomEndpoint")
    def public_ca_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubCustomEndpoint")
    def pubsub_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pubsubLiteCustomEndpoint")
    def pubsub_lite_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pulumiAttributionLabelAdditionStrategy")
    def pulumi_attribution_label_addition_strategy(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="recaptchaEnterpriseCustomEndpoint")
    def recaptcha_enterprise_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="redisCustomEndpoint")
    def redis_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestReason")
    def request_reason(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestTimeout")
    def request_timeout(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManager3CustomEndpoint")
    def resource_manager3_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerCustomEndpoint")
    def resource_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="resourceManagerV3CustomEndpoint")
    def resource_manager_v3_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeConfigCustomEndpoint")
    def runtime_config_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="runtimeconfigCustomEndpoint")
    def runtimeconfig_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="saasRuntimeCustomEndpoint")
    def saas_runtime_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerCustomEndpoint")
    def secret_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretManagerRegionalCustomEndpoint")
    def secret_manager_regional_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secureSourceManagerCustomEndpoint")
    def secure_source_manager_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterCustomEndpoint")
    def security_center_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterManagementCustomEndpoint")
    def security_center_management_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityCenterV2CustomEndpoint")
    def security_center_v2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityScannerCustomEndpoint")
    def security_scanner_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitypostureCustomEndpoint")
    def securityposture_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryCustomEndpoint")
    def service_directory_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceManagementCustomEndpoint")
    def service_management_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceNetworkingCustomEndpoint")
    def service_networking_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceUsageCustomEndpoint")
    def service_usage_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="siteVerificationCustomEndpoint")
    def site_verification_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sourceRepoCustomEndpoint")
    def source_repo_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="spannerCustomEndpoint")
    def spanner_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sqlCustomEndpoint")
    def sql_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageBatchOperationsCustomEndpoint")
    def storage_batch_operations_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageControlCustomEndpoint")
    def storage_control_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageCustomEndpoint")
    def storage_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageInsightsCustomEndpoint")
    def storage_insights_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="storageTransferCustomEndpoint")
    def storage_transfer_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsCustomEndpoint")
    def tags_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsLocationCustomEndpoint")
    def tags_location_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tpuV2CustomEndpoint")
    def tpu_v2_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="transcoderCustomEndpoint")
    def transcoder_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="universeDomain")
    def universe_domain(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vectorSearchCustomEndpoint")
    def vector_search_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vertexAiCustomEndpoint")
    def vertex_ai_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vmwareengineCustomEndpoint")
    def vmwareengine_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="vpcAccessCustomEndpoint")
    def vpc_access_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workbenchCustomEndpoint")
    def workbench_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workflowsCustomEndpoint")
    def workflows_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="workstationsCustomEndpoint")
    def workstations_custom_endpoint(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        ...
    
    @pulumi.output_type
    class TerraformConfigResult:
        def __init__(__self__, result=...) -> None:
            ...
        
        @_builtins.property
        @pulumi.getter
        def result(self) -> Mapping[str, Any]:
            ...
        
    
    
    def terraform_config(__self__) -> pulumi.Output[Provider.TerraformConfigResult]:
        
        ...
    


