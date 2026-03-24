import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountSettingsTimeoutsArgs",
    "AccountSettingsTimeoutsArgsDict",
    "AnalysisParametersArgs",
    "AnalysisParametersArgsDict",
    "AnalysisParametersDateTimeParameterArgs",
    "AnalysisParametersDateTimeParameterArgsDict",
    "AnalysisParametersDecimalParameterArgs",
    "AnalysisParametersDecimalParameterArgsDict",
    "AnalysisParametersIntegerParameterArgs",
    "AnalysisParametersIntegerParameterArgsDict",
    "AnalysisParametersStringParameterArgs",
    "AnalysisParametersStringParameterArgsDict",
    "AnalysisPermissionArgs",
    "AnalysisPermissionArgsDict",
    "AnalysisSourceEntityArgs",
    "AnalysisSourceEntityArgsDict",
    "AnalysisSourceEntitySourceTemplateArgs",
    "AnalysisSourceEntitySourceTemplateArgsDict",
    ...,
    ...,
    "CustomPermissionsCapabilitiesArgs",
    "CustomPermissionsCapabilitiesArgsDict",
    "DashboardDashboardPublishOptionsArgs",
    "DashboardDashboardPublishOptionsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DashboardParametersArgs",
    "DashboardParametersArgsDict",
    "DashboardParametersDateTimeParameterArgs",
    "DashboardParametersDateTimeParameterArgsDict",
    "DashboardParametersDecimalParameterArgs",
    "DashboardParametersDecimalParameterArgsDict",
    "DashboardParametersIntegerParameterArgs",
    "DashboardParametersIntegerParameterArgsDict",
    "DashboardParametersStringParameterArgs",
    "DashboardParametersStringParameterArgsDict",
    "DashboardPermissionArgs",
    "DashboardPermissionArgsDict",
    "DashboardSourceEntityArgs",
    "DashboardSourceEntityArgsDict",
    "DashboardSourceEntitySourceTemplateArgs",
    "DashboardSourceEntitySourceTemplateArgsDict",
    ...,
    ...,
    "DataSetColumnGroupArgs",
    "DataSetColumnGroupArgsDict",
    "DataSetColumnGroupGeoSpatialColumnGroupArgs",
    "DataSetColumnGroupGeoSpatialColumnGroupArgsDict",
    "DataSetColumnLevelPermissionRuleArgs",
    "DataSetColumnLevelPermissionRuleArgsDict",
    "DataSetDataSetUsageConfigurationArgs",
    "DataSetDataSetUsageConfigurationArgsDict",
    "DataSetFieldFolderArgs",
    "DataSetFieldFolderArgsDict",
    "DataSetLogicalTableMapArgs",
    "DataSetLogicalTableMapArgsDict",
    "DataSetLogicalTableMapDataTransformArgs",
    "DataSetLogicalTableMapDataTransformArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DataSetLogicalTableMapSourceArgs",
    "DataSetLogicalTableMapSourceArgsDict",
    "DataSetLogicalTableMapSourceJoinInstructionArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "DataSetOutputColumnArgs",
    "DataSetOutputColumnArgsDict",
    "DataSetPermissionArgs",
    "DataSetPermissionArgsDict",
    "DataSetPhysicalTableMapArgs",
    "DataSetPhysicalTableMapArgsDict",
    "DataSetPhysicalTableMapCustomSqlArgs",
    "DataSetPhysicalTableMapCustomSqlArgsDict",
    "DataSetPhysicalTableMapCustomSqlColumnArgs",
    "DataSetPhysicalTableMapCustomSqlColumnArgsDict",
    "DataSetPhysicalTableMapRelationalTableArgs",
    "DataSetPhysicalTableMapRelationalTableArgsDict",
    ...,
    ...,
    "DataSetPhysicalTableMapS3SourceArgs",
    "DataSetPhysicalTableMapS3SourceArgsDict",
    "DataSetPhysicalTableMapS3SourceInputColumnArgs",
    "DataSetPhysicalTableMapS3SourceInputColumnArgsDict",
    "DataSetPhysicalTableMapS3SourceUploadSettingsArgs",
    ...,
    "DataSetRefreshPropertiesArgs",
    "DataSetRefreshPropertiesArgsDict",
    "DataSetRefreshPropertiesRefreshConfigurationArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "DataSetRowLevelPermissionDataSetArgs",
    "DataSetRowLevelPermissionDataSetArgsDict",
    "DataSetRowLevelPermissionTagConfigurationArgs",
    "DataSetRowLevelPermissionTagConfigurationArgsDict",
    ...,
    ...,
    "DataSourceCredentialsArgs",
    "DataSourceCredentialsArgsDict",
    "DataSourceCredentialsCredentialPairArgs",
    "DataSourceCredentialsCredentialPairArgsDict",
    "DataSourceParametersArgs",
    "DataSourceParametersArgsDict",
    "DataSourceParametersAmazonElasticsearchArgs",
    "DataSourceParametersAmazonElasticsearchArgsDict",
    "DataSourceParametersAthenaArgs",
    "DataSourceParametersAthenaArgsDict",
    "DataSourceParametersAuroraArgs",
    "DataSourceParametersAuroraArgsDict",
    "DataSourceParametersAuroraPostgresqlArgs",
    "DataSourceParametersAuroraPostgresqlArgsDict",
    "DataSourceParametersAwsIotAnalyticsArgs",
    "DataSourceParametersAwsIotAnalyticsArgsDict",
    "DataSourceParametersDatabricksArgs",
    "DataSourceParametersDatabricksArgsDict",
    "DataSourceParametersJiraArgs",
    "DataSourceParametersJiraArgsDict",
    "DataSourceParametersMariaDbArgs",
    "DataSourceParametersMariaDbArgsDict",
    "DataSourceParametersMysqlArgs",
    "DataSourceParametersMysqlArgsDict",
    "DataSourceParametersOracleArgs",
    "DataSourceParametersOracleArgsDict",
    "DataSourceParametersPostgresqlArgs",
    "DataSourceParametersPostgresqlArgsDict",
    "DataSourceParametersPrestoArgs",
    "DataSourceParametersPrestoArgsDict",
    "DataSourceParametersRdsArgs",
    "DataSourceParametersRdsArgsDict",
    "DataSourceParametersRedshiftArgs",
    "DataSourceParametersRedshiftArgsDict",
    "DataSourceParametersS3Args",
    "DataSourceParametersS3ArgsDict",
    "DataSourceParametersS3ManifestFileLocationArgs",
    "DataSourceParametersS3ManifestFileLocationArgsDict",
    "DataSourceParametersServiceNowArgs",
    "DataSourceParametersServiceNowArgsDict",
    "DataSourceParametersSnowflakeArgs",
    "DataSourceParametersSnowflakeArgsDict",
    "DataSourceParametersSparkArgs",
    "DataSourceParametersSparkArgsDict",
    "DataSourceParametersSqlServerArgs",
    "DataSourceParametersSqlServerArgsDict",
    "DataSourceParametersTeradataArgs",
    "DataSourceParametersTeradataArgsDict",
    "DataSourceParametersTwitterArgs",
    "DataSourceParametersTwitterArgsDict",
    "DataSourcePermissionArgs",
    "DataSourcePermissionArgsDict",
    "DataSourceSslPropertiesArgs",
    "DataSourceSslPropertiesArgsDict",
    "DataSourceVpcConnectionPropertiesArgs",
    "DataSourceVpcConnectionPropertiesArgsDict",
    "FolderPermissionArgs",
    "FolderPermissionArgsDict",
    "IamPolicyAssignmentIdentitiesArgs",
    "IamPolicyAssignmentIdentitiesArgsDict",
    "KeyRegistrationKeyRegistrationArgs",
    "KeyRegistrationKeyRegistrationArgsDict",
    "NamespaceTimeoutsArgs",
    "NamespaceTimeoutsArgsDict",
    "RefreshScheduleScheduleArgs",
    "RefreshScheduleScheduleArgsDict",
    "RefreshScheduleScheduleScheduleFrequencyArgs",
    "RefreshScheduleScheduleScheduleFrequencyArgsDict",
    ...,
    ...,
    "TemplatePermissionArgs",
    "TemplatePermissionArgsDict",
    "TemplateSourceEntityArgs",
    "TemplateSourceEntityArgsDict",
    "TemplateSourceEntitySourceAnalysisArgs",
    "TemplateSourceEntitySourceAnalysisArgsDict",
    ...,
    ...,
    "TemplateSourceEntitySourceTemplateArgs",
    "TemplateSourceEntitySourceTemplateArgsDict",
    "ThemeConfigurationArgs",
    "ThemeConfigurationArgsDict",
    "ThemeConfigurationDataColorPaletteArgs",
    "ThemeConfigurationDataColorPaletteArgsDict",
    "ThemeConfigurationSheetArgs",
    "ThemeConfigurationSheetArgsDict",
    "ThemeConfigurationSheetTileArgs",
    "ThemeConfigurationSheetTileArgsDict",
    "ThemeConfigurationSheetTileBorderArgs",
    "ThemeConfigurationSheetTileBorderArgsDict",
    "ThemeConfigurationSheetTileLayoutArgs",
    "ThemeConfigurationSheetTileLayoutArgsDict",
    "ThemeConfigurationSheetTileLayoutGutterArgs",
    "ThemeConfigurationSheetTileLayoutGutterArgsDict",
    "ThemeConfigurationSheetTileLayoutMarginArgs",
    "ThemeConfigurationSheetTileLayoutMarginArgsDict",
    "ThemeConfigurationTypographyArgs",
    "ThemeConfigurationTypographyArgsDict",
    "ThemeConfigurationTypographyFontFamilyArgs",
    "ThemeConfigurationTypographyFontFamilyArgsDict",
    "ThemeConfigurationUiColorPaletteArgs",
    "ThemeConfigurationUiColorPaletteArgsDict",
    "ThemePermissionArgs",
    "ThemePermissionArgsDict",
    "VpcConnectionTimeoutsArgs",
    "VpcConnectionTimeoutsArgsDict",
]

class AccountSettingsTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AccountSettingsTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AnalysisParametersArgsDict(TypedDict):
    date_time_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AnalysisParametersDateTimeParameterArgsDict]]
        ]
    ]
    decimal_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersDecimalParameterArgsDict]]]
    ]
    integer_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersIntegerParameterArgsDict]]]
    ]
    string_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersStringParameterArgsDict]]]
    ]
    ...

@pulumi.input_type
class AnalysisParametersArgs:
    def __init__(
        __self__,
        *,
        date_time_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AnalysisParametersDateTimeParameterArgs]]
            ]
        ] = ...,
        decimal_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersDecimalParameterArgs]]]
        ] = ...,
        integer_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersIntegerParameterArgs]]]
        ] = ...,
        string_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersStringParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeParameters")
    def date_time_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersDateTimeParameterArgs]]]
    ]: ...
    @date_time_parameters.setter
    def date_time_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AnalysisParametersDateTimeParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="decimalParameters")
    def decimal_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersDecimalParameterArgs]]]
    ]: ...
    @decimal_parameters.setter
    def decimal_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersDecimalParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerParameters")
    def integer_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersIntegerParameterArgs]]]
    ]: ...
    @integer_parameters.setter
    def integer_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersIntegerParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringParameters")
    def string_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AnalysisParametersStringParameterArgs]]]
    ]: ...
    @string_parameters.setter
    def string_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AnalysisParametersStringParameterArgs]]]
        ],
    ): ...

class AnalysisParametersDateTimeParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class AnalysisParametersDateTimeParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class AnalysisParametersDecimalParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]
    ...

@pulumi.input_type
class AnalysisParametersDecimalParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]): ...

class AnalysisParametersIntegerParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class AnalysisParametersIntegerParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...

class AnalysisParametersStringParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class AnalysisParametersStringParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class AnalysisPermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AnalysisPermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class AnalysisSourceEntityArgsDict(TypedDict):
    source_template: NotRequired[
        pulumi.Input[AnalysisSourceEntitySourceTemplateArgsDict]
    ]
    ...

@pulumi.input_type
class AnalysisSourceEntityArgs:
    def __init__(
        __self__,
        *,
        source_template: Optional[
            pulumi.Input[AnalysisSourceEntitySourceTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[pulumi.Input[AnalysisSourceEntitySourceTemplateArgs]]: ...
    @source_template.setter
    def source_template(
        self, value: Optional[pulumi.Input[AnalysisSourceEntitySourceTemplateArgs]]
    ): ...

class AnalysisSourceEntitySourceTemplateArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    data_set_references: pulumi.Input[
        Sequence[
            pulumi.Input[AnalysisSourceEntitySourceTemplateDataSetReferenceArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class AnalysisSourceEntitySourceTemplateArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        data_set_references: pulumi.Input[
            Sequence[
                pulumi.Input[AnalysisSourceEntitySourceTemplateDataSetReferenceArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[AnalysisSourceEntitySourceTemplateDataSetReferenceArgs]]
    ]: ...
    @data_set_references.setter
    def data_set_references(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[AnalysisSourceEntitySourceTemplateDataSetReferenceArgs]
            ]
        ],
    ): ...

class AnalysisSourceEntitySourceTemplateDataSetReferenceArgsDict(TypedDict):
    data_set_arn: pulumi.Input[_builtins.str]
    data_set_placeholder: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class AnalysisSourceEntitySourceTemplateDataSetReferenceArgs:
    def __init__(
        __self__,
        *,
        data_set_arn: pulumi.Input[_builtins.str],
        data_set_placeholder: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_arn.setter
    def data_set_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_placeholder.setter
    def data_set_placeholder(self, value: pulumi.Input[_builtins.str]): ...

class CustomPermissionsCapabilitiesArgsDict(TypedDict):
    add_or_run_anomaly_detection_for_analyses: NotRequired[pulumi.Input[_builtins.str]]
    create_and_update_dashboard_email_reports: NotRequired[pulumi.Input[_builtins.str]]
    create_and_update_data_sources: NotRequired[pulumi.Input[_builtins.str]]
    create_and_update_datasets: NotRequired[pulumi.Input[_builtins.str]]
    create_and_update_themes: NotRequired[pulumi.Input[_builtins.str]]
    create_and_update_threshold_alerts: NotRequired[pulumi.Input[_builtins.str]]
    create_shared_folders: NotRequired[pulumi.Input[_builtins.str]]
    create_spice_dataset: NotRequired[pulumi.Input[_builtins.str]]
    export_to_csv: NotRequired[pulumi.Input[_builtins.str]]
    export_to_csv_in_scheduled_reports: NotRequired[pulumi.Input[_builtins.str]]
    export_to_excel: NotRequired[pulumi.Input[_builtins.str]]
    export_to_excel_in_scheduled_reports: NotRequired[pulumi.Input[_builtins.str]]
    export_to_pdf: NotRequired[pulumi.Input[_builtins.str]]
    export_to_pdf_in_scheduled_reports: NotRequired[pulumi.Input[_builtins.str]]
    include_content_in_scheduled_reports_email: NotRequired[pulumi.Input[_builtins.str]]
    print_reports: NotRequired[pulumi.Input[_builtins.str]]
    rename_shared_folders: NotRequired[pulumi.Input[_builtins.str]]
    share_analyses: NotRequired[pulumi.Input[_builtins.str]]
    share_dashboards: NotRequired[pulumi.Input[_builtins.str]]
    share_data_sources: NotRequired[pulumi.Input[_builtins.str]]
    share_datasets: NotRequired[pulumi.Input[_builtins.str]]
    subscribe_dashboard_email_reports: NotRequired[pulumi.Input[_builtins.str]]
    view_account_spice_capacity: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class CustomPermissionsCapabilitiesArgs:
    def __init__(
        __self__,
        *,
        add_or_run_anomaly_detection_for_analyses: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        create_and_update_dashboard_email_reports: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        create_and_update_data_sources: Optional[pulumi.Input[_builtins.str]] = ...,
        create_and_update_datasets: Optional[pulumi.Input[_builtins.str]] = ...,
        create_and_update_themes: Optional[pulumi.Input[_builtins.str]] = ...,
        create_and_update_threshold_alerts: Optional[pulumi.Input[_builtins.str]] = ...,
        create_shared_folders: Optional[pulumi.Input[_builtins.str]] = ...,
        create_spice_dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_csv: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_csv_in_scheduled_reports: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_excel: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_excel_in_scheduled_reports: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        export_to_pdf: Optional[pulumi.Input[_builtins.str]] = ...,
        export_to_pdf_in_scheduled_reports: Optional[pulumi.Input[_builtins.str]] = ...,
        include_content_in_scheduled_reports_email: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        print_reports: Optional[pulumi.Input[_builtins.str]] = ...,
        rename_shared_folders: Optional[pulumi.Input[_builtins.str]] = ...,
        share_analyses: Optional[pulumi.Input[_builtins.str]] = ...,
        share_dashboards: Optional[pulumi.Input[_builtins.str]] = ...,
        share_data_sources: Optional[pulumi.Input[_builtins.str]] = ...,
        share_datasets: Optional[pulumi.Input[_builtins.str]] = ...,
        subscribe_dashboard_email_reports: Optional[pulumi.Input[_builtins.str]] = ...,
        view_account_spice_capacity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addOrRunAnomalyDetectionForAnalyses")
    def add_or_run_anomaly_detection_for_analyses(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @add_or_run_anomaly_detection_for_analyses.setter
    def add_or_run_anomaly_detection_for_analyses(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDashboardEmailReports")
    def create_and_update_dashboard_email_reports(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_and_update_dashboard_email_reports.setter
    def create_and_update_dashboard_email_reports(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDataSources")
    def create_and_update_data_sources(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_and_update_data_sources.setter
    def create_and_update_data_sources(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDatasets")
    def create_and_update_datasets(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_and_update_datasets.setter
    def create_and_update_datasets(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateThemes")
    def create_and_update_themes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_and_update_themes.setter
    def create_and_update_themes(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateThresholdAlerts")
    def create_and_update_threshold_alerts(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_and_update_threshold_alerts.setter
    def create_and_update_threshold_alerts(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createSharedFolders")
    def create_shared_folders(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_shared_folders.setter
    def create_shared_folders(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createSpiceDataset")
    def create_spice_dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_spice_dataset.setter
    def create_spice_dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportToCsv")
    def export_to_csv(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_csv.setter
    def export_to_csv(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportToCsvInScheduledReports")
    def export_to_csv_in_scheduled_reports(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_csv_in_scheduled_reports.setter
    def export_to_csv_in_scheduled_reports(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportToExcel")
    def export_to_excel(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_excel.setter
    def export_to_excel(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportToExcelInScheduledReports")
    def export_to_excel_in_scheduled_reports(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_excel_in_scheduled_reports.setter
    def export_to_excel_in_scheduled_reports(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportToPdf")
    def export_to_pdf(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_pdf.setter
    def export_to_pdf(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="exportToPdfInScheduledReports")
    def export_to_pdf_in_scheduled_reports(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @export_to_pdf_in_scheduled_reports.setter
    def export_to_pdf_in_scheduled_reports(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="includeContentInScheduledReportsEmail")
    def include_content_in_scheduled_reports_email(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @include_content_in_scheduled_reports_email.setter
    def include_content_in_scheduled_reports_email(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="printReports")
    def print_reports(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @print_reports.setter
    def print_reports(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="renameSharedFolders")
    def rename_shared_folders(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @rename_shared_folders.setter
    def rename_shared_folders(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareAnalyses")
    def share_analyses(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_analyses.setter
    def share_analyses(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareDashboards")
    def share_dashboards(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_dashboards.setter
    def share_dashboards(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareDataSources")
    def share_data_sources(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_data_sources.setter
    def share_data_sources(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="shareDatasets")
    def share_datasets(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @share_datasets.setter
    def share_datasets(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subscribeDashboardEmailReports")
    def subscribe_dashboard_email_reports(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subscribe_dashboard_email_reports.setter
    def subscribe_dashboard_email_reports(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="viewAccountSpiceCapacity")
    def view_account_spice_capacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @view_account_spice_capacity.setter
    def view_account_spice_capacity(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DashboardDashboardPublishOptionsArgsDict(TypedDict):
    ad_hoc_filtering_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsAdHocFilteringOptionArgsDict]
    ]
    data_point_drill_up_down_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgsDict]
    ]
    data_point_menu_label_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgsDict]
    ]
    data_point_tooltip_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointTooltipOptionArgsDict]
    ]
    export_to_csv_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsExportToCsvOptionArgsDict]
    ]
    export_with_hidden_fields_option: NotRequired[
        pulumi.Input[
            DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgsDict
        ]
    ]
    sheet_controls_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsSheetControlsOptionArgsDict]
    ]
    sheet_layout_element_maximization_option: NotRequired[
        pulumi.Input[
            DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgsDict
        ]
    ]
    visual_axis_sort_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsVisualAxisSortOptionArgsDict]
    ]
    visual_menu_option: NotRequired[
        pulumi.Input[DashboardDashboardPublishOptionsVisualMenuOptionArgsDict]
    ]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsArgs:
    def __init__(
        __self__,
        *,
        ad_hoc_filtering_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsAdHocFilteringOptionArgs]
        ] = ...,
        data_point_drill_up_down_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgs]
        ] = ...,
        data_point_menu_label_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgs]
        ] = ...,
        data_point_tooltip_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointTooltipOptionArgs]
        ] = ...,
        export_to_csv_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsExportToCsvOptionArgs]
        ] = ...,
        export_with_hidden_fields_option: Optional[
            pulumi.Input[
                DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgs
            ]
        ] = ...,
        sheet_controls_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsSheetControlsOptionArgs]
        ] = ...,
        sheet_layout_element_maximization_option: Optional[
            pulumi.Input[
                DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgs
            ]
        ] = ...,
        visual_axis_sort_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsVisualAxisSortOptionArgs]
        ] = ...,
        visual_menu_option: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsVisualMenuOptionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adHocFilteringOption")
    def ad_hoc_filtering_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsAdHocFilteringOptionArgs]
    ]: ...
    @ad_hoc_filtering_option.setter
    def ad_hoc_filtering_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsAdHocFilteringOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPointDrillUpDownOption")
    def data_point_drill_up_down_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgs]
    ]: ...
    @data_point_drill_up_down_option.setter
    def data_point_drill_up_down_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPointMenuLabelOption")
    def data_point_menu_label_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgs]
    ]: ...
    @data_point_menu_label_option.setter
    def data_point_menu_label_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataPointTooltipOption")
    def data_point_tooltip_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsDataPointTooltipOptionArgs]
    ]: ...
    @data_point_tooltip_option.setter
    def data_point_tooltip_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsDataPointTooltipOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportToCsvOption")
    def export_to_csv_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsExportToCsvOptionArgs]
    ]: ...
    @export_to_csv_option.setter
    def export_to_csv_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsExportToCsvOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="exportWithHiddenFieldsOption")
    def export_with_hidden_fields_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgs]
    ]: ...
    @export_with_hidden_fields_option.setter
    def export_with_hidden_fields_option(
        self,
        value: Optional[
            pulumi.Input[
                DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sheetControlsOption")
    def sheet_controls_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsSheetControlsOptionArgs]
    ]: ...
    @sheet_controls_option.setter
    def sheet_controls_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsSheetControlsOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="sheetLayoutElementMaximizationOption")
    def sheet_layout_element_maximization_option(
        self,
    ) -> Optional[
        pulumi.Input[
            DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgs
        ]
    ]: ...
    @sheet_layout_element_maximization_option.setter
    def sheet_layout_element_maximization_option(
        self,
        value: Optional[
            pulumi.Input[
                DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="visualAxisSortOption")
    def visual_axis_sort_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsVisualAxisSortOptionArgs]
    ]: ...
    @visual_axis_sort_option.setter
    def visual_axis_sort_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsVisualAxisSortOptionArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="visualMenuOption")
    def visual_menu_option(
        self,
    ) -> Optional[
        pulumi.Input[DashboardDashboardPublishOptionsVisualMenuOptionArgs]
    ]: ...
    @visual_menu_option.setter
    def visual_menu_option(
        self,
        value: Optional[
            pulumi.Input[DashboardDashboardPublishOptionsVisualMenuOptionArgs]
        ],
    ): ...

class DashboardDashboardPublishOptionsAdHocFilteringOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsAdHocFilteringOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsDataPointDrillUpDownOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsDataPointMenuLabelOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsDataPointTooltipOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsDataPointTooltipOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsExportToCsvOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsExportToCsvOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsExportWithHiddenFieldsOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsSheetControlsOptionArgsDict(TypedDict):
    visibility_state: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsSheetControlsOptionArgs:
    def __init__(
        __self__, *, visibility_state: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="visibilityState")
    def visibility_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @visibility_state.setter
    def visibility_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgsDict(
    TypedDict
):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsVisualAxisSortOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsVisualAxisSortOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardDashboardPublishOptionsVisualMenuOptionArgsDict(TypedDict):
    availability_status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DashboardDashboardPublishOptionsVisualMenuOptionArgs:
    def __init__(
        __self__, *, availability_status: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @availability_status.setter
    def availability_status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DashboardParametersArgsDict(TypedDict):
    date_time_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DashboardParametersDateTimeParameterArgsDict]]
        ]
    ]
    decimal_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DashboardParametersDecimalParameterArgsDict]]
        ]
    ]
    integer_parameters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DashboardParametersIntegerParameterArgsDict]]
        ]
    ]
    string_parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[DashboardParametersStringParameterArgsDict]]]
    ]
    ...

@pulumi.input_type
class DashboardParametersArgs:
    def __init__(
        __self__,
        *,
        date_time_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersDateTimeParameterArgs]]
            ]
        ] = ...,
        decimal_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersDecimalParameterArgs]]
            ]
        ] = ...,
        integer_parameters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersIntegerParameterArgs]]
            ]
        ] = ...,
        string_parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[DashboardParametersStringParameterArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeParameters")
    def date_time_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DashboardParametersDateTimeParameterArgs]]]
    ]: ...
    @date_time_parameters.setter
    def date_time_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersDateTimeParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="decimalParameters")
    def decimal_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DashboardParametersDecimalParameterArgs]]]
    ]: ...
    @decimal_parameters.setter
    def decimal_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersDecimalParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="integerParameters")
    def integer_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DashboardParametersIntegerParameterArgs]]]
    ]: ...
    @integer_parameters.setter
    def integer_parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DashboardParametersIntegerParameterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="stringParameters")
    def string_parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DashboardParametersStringParameterArgs]]]
    ]: ...
    @string_parameters.setter
    def string_parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[DashboardParametersStringParameterArgs]]]
        ],
    ): ...

class DashboardParametersDateTimeParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DashboardParametersDateTimeParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DashboardParametersDecimalParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]
    ...

@pulumi.input_type
class DashboardParametersDecimalParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.float]]]): ...

class DashboardParametersIntegerParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]
    ...

@pulumi.input_type
class DashboardParametersIntegerParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.int]]]): ...

class DashboardParametersStringParameterArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DashboardParametersStringParameterArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        values: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DashboardPermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DashboardPermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class DashboardSourceEntityArgsDict(TypedDict):
    source_template: NotRequired[
        pulumi.Input[DashboardSourceEntitySourceTemplateArgsDict]
    ]
    ...

@pulumi.input_type
class DashboardSourceEntityArgs:
    def __init__(
        __self__,
        *,
        source_template: Optional[
            pulumi.Input[DashboardSourceEntitySourceTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[pulumi.Input[DashboardSourceEntitySourceTemplateArgs]]: ...
    @source_template.setter
    def source_template(
        self, value: Optional[pulumi.Input[DashboardSourceEntitySourceTemplateArgs]]
    ): ...

class DashboardSourceEntitySourceTemplateArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    data_set_references: pulumi.Input[
        Sequence[
            pulumi.Input[DashboardSourceEntitySourceTemplateDataSetReferenceArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class DashboardSourceEntitySourceTemplateArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        data_set_references: pulumi.Input[
            Sequence[
                pulumi.Input[DashboardSourceEntitySourceTemplateDataSetReferenceArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[DashboardSourceEntitySourceTemplateDataSetReferenceArgs]]
    ]: ...
    @data_set_references.setter
    def data_set_references(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[DashboardSourceEntitySourceTemplateDataSetReferenceArgs]
            ]
        ],
    ): ...

class DashboardSourceEntitySourceTemplateDataSetReferenceArgsDict(TypedDict):
    data_set_arn: pulumi.Input[_builtins.str]
    data_set_placeholder: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DashboardSourceEntitySourceTemplateDataSetReferenceArgs:
    def __init__(
        __self__,
        *,
        data_set_arn: pulumi.Input[_builtins.str],
        data_set_placeholder: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_arn.setter
    def data_set_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_placeholder.setter
    def data_set_placeholder(self, value: pulumi.Input[_builtins.str]): ...

class DataSetColumnGroupArgsDict(TypedDict):
    geo_spatial_column_group: NotRequired[
        pulumi.Input[DataSetColumnGroupGeoSpatialColumnGroupArgsDict]
    ]
    ...

@pulumi.input_type
class DataSetColumnGroupArgs:
    def __init__(
        __self__,
        *,
        geo_spatial_column_group: Optional[
            pulumi.Input[DataSetColumnGroupGeoSpatialColumnGroupArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoSpatialColumnGroup")
    def geo_spatial_column_group(
        self,
    ) -> Optional[pulumi.Input[DataSetColumnGroupGeoSpatialColumnGroupArgs]]: ...
    @geo_spatial_column_group.setter
    def geo_spatial_column_group(
        self, value: Optional[pulumi.Input[DataSetColumnGroupGeoSpatialColumnGroupArgs]]
    ): ...

class DataSetColumnGroupGeoSpatialColumnGroupArgsDict(TypedDict):
    columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    country_code: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetColumnGroupGeoSpatialColumnGroupArgs:
    def __init__(
        __self__,
        *,
        columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        country_code: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @columns.setter
    def columns(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> pulumi.Input[_builtins.str]: ...
    @country_code.setter
    def country_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...

class DataSetColumnLevelPermissionRuleArgsDict(TypedDict):
    column_names: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class DataSetColumnLevelPermissionRuleArgs:
    def __init__(
        __self__,
        *,
        column_names: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        principals: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @column_names.setter
    def column_names(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def principals(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @principals.setter
    def principals(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataSetDataSetUsageConfigurationArgsDict(TypedDict):
    disable_use_as_direct_query_source: NotRequired[pulumi.Input[_builtins.bool]]
    disable_use_as_imported_source: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DataSetDataSetUsageConfigurationArgs:
    def __init__(
        __self__,
        *,
        disable_use_as_direct_query_source: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        disable_use_as_imported_source: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsDirectQuerySource")
    def disable_use_as_direct_query_source(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_use_as_direct_query_source.setter
    def disable_use_as_direct_query_source(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsImportedSource")
    def disable_use_as_imported_source(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_use_as_imported_source.setter
    def disable_use_as_imported_source(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DataSetFieldFolderArgsDict(TypedDict):
    field_folders_id: pulumi.Input[_builtins.str]
    columns: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetFieldFolderArgs:
    def __init__(
        __self__,
        *,
        field_folders_id: pulumi.Input[_builtins.str],
        columns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldFoldersId")
    def field_folders_id(self) -> pulumi.Input[_builtins.str]: ...
    @field_folders_id.setter
    def field_folders_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @columns.setter
    def columns(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetLogicalTableMapArgsDict(TypedDict):
    alias: pulumi.Input[_builtins.str]
    logical_table_map_id: pulumi.Input[_builtins.str]
    source: pulumi.Input[DataSetLogicalTableMapSourceArgsDict]
    data_transforms: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DataSetLogicalTableMapDataTransformArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class DataSetLogicalTableMapArgs:
    def __init__(
        __self__,
        *,
        alias: pulumi.Input[_builtins.str],
        logical_table_map_id: pulumi.Input[_builtins.str],
        source: pulumi.Input[DataSetLogicalTableMapSourceArgs],
        data_transforms: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataSetLogicalTableMapDataTransformArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> pulumi.Input[_builtins.str]: ...
    @alias.setter
    def alias(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="logicalTableMapId")
    def logical_table_map_id(self) -> pulumi.Input[_builtins.str]: ...
    @logical_table_map_id.setter
    def logical_table_map_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[DataSetLogicalTableMapSourceArgs]: ...
    @source.setter
    def source(self, value: pulumi.Input[DataSetLogicalTableMapSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="dataTransforms")
    def data_transforms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DataSetLogicalTableMapDataTransformArgs]]]
    ]: ...
    @data_transforms.setter
    def data_transforms(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataSetLogicalTableMapDataTransformArgs]]
            ]
        ],
    ): ...

class DataSetLogicalTableMapDataTransformArgsDict(TypedDict):
    cast_column_type_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgsDict]
    ]
    create_columns_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformCreateColumnsOperationArgsDict]
    ]
    filter_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformFilterOperationArgsDict]
    ]
    project_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformProjectOperationArgsDict]
    ]
    rename_column_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformRenameColumnOperationArgsDict]
    ]
    tag_column_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformTagColumnOperationArgsDict]
    ]
    untag_column_operation: NotRequired[
        pulumi.Input[DataSetLogicalTableMapDataTransformUntagColumnOperationArgsDict]
    ]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformArgs:
    def __init__(
        __self__,
        *,
        cast_column_type_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgs]
        ] = ...,
        create_columns_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformCreateColumnsOperationArgs]
        ] = ...,
        filter_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformFilterOperationArgs]
        ] = ...,
        project_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformProjectOperationArgs]
        ] = ...,
        rename_column_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformRenameColumnOperationArgs]
        ] = ...,
        tag_column_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformTagColumnOperationArgs]
        ] = ...,
        untag_column_operation: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformUntagColumnOperationArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="castColumnTypeOperation")
    def cast_column_type_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgs]
    ]: ...
    @cast_column_type_operation.setter
    def cast_column_type_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createColumnsOperation")
    def create_columns_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformCreateColumnsOperationArgs]
    ]: ...
    @create_columns_operation.setter
    def create_columns_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformCreateColumnsOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="filterOperation")
    def filter_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformFilterOperationArgs]
    ]: ...
    @filter_operation.setter
    def filter_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformFilterOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="projectOperation")
    def project_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformProjectOperationArgs]
    ]: ...
    @project_operation.setter
    def project_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformProjectOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="renameColumnOperation")
    def rename_column_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformRenameColumnOperationArgs]
    ]: ...
    @rename_column_operation.setter
    def rename_column_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformRenameColumnOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagColumnOperation")
    def tag_column_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformTagColumnOperationArgs]
    ]: ...
    @tag_column_operation.setter
    def tag_column_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformTagColumnOperationArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="untagColumnOperation")
    def untag_column_operation(
        self,
    ) -> Optional[
        pulumi.Input[DataSetLogicalTableMapDataTransformUntagColumnOperationArgs]
    ]: ...
    @untag_column_operation.setter
    def untag_column_operation(
        self,
        value: Optional[
            pulumi.Input[DataSetLogicalTableMapDataTransformUntagColumnOperationArgs]
        ],
    ): ...

class DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    new_column_type: pulumi.Input[_builtins.str]
    format: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformCastColumnTypeOperationArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        new_column_type: pulumi.Input[_builtins.str],
        format: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="newColumnType")
    def new_column_type(self) -> pulumi.Input[_builtins.str]: ...
    @new_column_type.setter
    def new_column_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetLogicalTableMapDataTransformCreateColumnsOperationArgsDict(TypedDict):
    columns: pulumi.Input[
        Sequence[
            pulumi.Input[
                DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformCreateColumnsOperationArgs:
    def __init__(
        __self__,
        *,
        columns: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[
                DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgs
            ]
        ]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgs
                ]
            ]
        ],
    ): ...

class DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgsDict(
    TypedDict
):
    column_id: pulumi.Input[_builtins.str]
    column_name: pulumi.Input[_builtins.str]
    expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformCreateColumnsOperationColumnArgs:
    def __init__(
        __self__,
        *,
        column_id: pulumi.Input[_builtins.str],
        column_name: pulumi.Input[_builtins.str],
        expression: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnId")
    def column_id(self) -> pulumi.Input[_builtins.str]: ...
    @column_id.setter
    def column_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...

class DataSetLogicalTableMapDataTransformFilterOperationArgsDict(TypedDict):
    condition_expression: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformFilterOperationArgs:
    def __init__(
        __self__, *, condition_expression: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> pulumi.Input[_builtins.str]: ...
    @condition_expression.setter
    def condition_expression(self, value: pulumi.Input[_builtins.str]): ...

class DataSetLogicalTableMapDataTransformProjectOperationArgsDict(TypedDict):
    projected_columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformProjectOperationArgs:
    def __init__(
        __self__,
        *,
        projected_columns: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectedColumns")
    def projected_columns(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @projected_columns.setter
    def projected_columns(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...

class DataSetLogicalTableMapDataTransformRenameColumnOperationArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    new_column_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformRenameColumnOperationArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        new_column_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="newColumnName")
    def new_column_name(self) -> pulumi.Input[_builtins.str]: ...
    @new_column_name.setter
    def new_column_name(self, value: pulumi.Input[_builtins.str]): ...

class DataSetLogicalTableMapDataTransformTagColumnOperationArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    tags: pulumi.Input[
        Sequence[
            pulumi.Input[
                DataSetLogicalTableMapDataTransformTagColumnOperationTagArgsDict
            ]
        ]
    ]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformTagColumnOperationArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        tags: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSetLogicalTableMapDataTransformTagColumnOperationTagArgs
                ]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> pulumi.Input[
        Sequence[
            pulumi.Input[DataSetLogicalTableMapDataTransformTagColumnOperationTagArgs]
        ]
    ]: ...
    @tags.setter
    def tags(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataSetLogicalTableMapDataTransformTagColumnOperationTagArgs
                ]
            ]
        ],
    ): ...

class DataSetLogicalTableMapDataTransformTagColumnOperationTagArgsDict(TypedDict):
    column_description: NotRequired[
        pulumi.Input[
            DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgsDict
        ]
    ]
    column_geographic_role: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformTagColumnOperationTagArgs:
    def __init__(
        __self__,
        *,
        column_description: Optional[
            pulumi.Input[
                DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgs
            ]
        ] = ...,
        column_geographic_role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnDescription")
    def column_description(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgs
        ]
    ]: ...
    @column_description.setter
    def column_description(
        self,
        value: Optional[
            pulumi.Input[
                DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="columnGeographicRole")
    def column_geographic_role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @column_geographic_role.setter
    def column_geographic_role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgsDict(
    TypedDict
):
    text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionArgs:
    def __init__(
        __self__, *, text: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetLogicalTableMapDataTransformUntagColumnOperationArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    tag_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapDataTransformUntagColumnOperationArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        tag_names: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagNames")
    def tag_names(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @tag_names.setter
    def tag_names(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...

class DataSetLogicalTableMapSourceArgsDict(TypedDict):
    data_set_arn: NotRequired[pulumi.Input[_builtins.str]]
    join_instruction: NotRequired[
        pulumi.Input[DataSetLogicalTableMapSourceJoinInstructionArgsDict]
    ]
    physical_table_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapSourceArgs:
    def __init__(
        __self__,
        *,
        data_set_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        join_instruction: Optional[
            pulumi.Input[DataSetLogicalTableMapSourceJoinInstructionArgs]
        ] = ...,
        physical_table_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_set_arn.setter
    def data_set_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="joinInstruction")
    def join_instruction(
        self,
    ) -> Optional[pulumi.Input[DataSetLogicalTableMapSourceJoinInstructionArgs]]: ...
    @join_instruction.setter
    def join_instruction(
        self,
        value: Optional[pulumi.Input[DataSetLogicalTableMapSourceJoinInstructionArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="physicalTableId")
    def physical_table_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @physical_table_id.setter
    def physical_table_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetLogicalTableMapSourceJoinInstructionArgsDict(TypedDict):
    left_operand: pulumi.Input[_builtins.str]
    on_clause: pulumi.Input[_builtins.str]
    right_operand: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    left_join_key_properties: NotRequired[
        pulumi.Input[
            DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgsDict
        ]
    ]
    right_join_key_properties: NotRequired[
        pulumi.Input[
            DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgsDict
        ]
    ]
    ...

@pulumi.input_type
class DataSetLogicalTableMapSourceJoinInstructionArgs:
    def __init__(
        __self__,
        *,
        left_operand: pulumi.Input[_builtins.str],
        on_clause: pulumi.Input[_builtins.str],
        right_operand: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
        left_join_key_properties: Optional[
            pulumi.Input[
                DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgs
            ]
        ] = ...,
        right_join_key_properties: Optional[
            pulumi.Input[
                DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leftOperand")
    def left_operand(self) -> pulumi.Input[_builtins.str]: ...
    @left_operand.setter
    def left_operand(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="onClause")
    def on_clause(self) -> pulumi.Input[_builtins.str]: ...
    @on_clause.setter
    def on_clause(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="rightOperand")
    def right_operand(self) -> pulumi.Input[_builtins.str]: ...
    @right_operand.setter
    def right_operand(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="leftJoinKeyProperties")
    def left_join_key_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgs
        ]
    ]: ...
    @left_join_key_properties.setter
    def left_join_key_properties(
        self,
        value: Optional[
            pulumi.Input[
                DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rightJoinKeyProperties")
    def right_join_key_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgs
        ]
    ]: ...
    @right_join_key_properties.setter
    def right_join_key_properties(
        self,
        value: Optional[
            pulumi.Input[
                DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgs
            ]
        ],
    ): ...

class DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgsDict(
    TypedDict
):
    unique_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertiesArgs:
    def __init__(
        __self__, *, unique_key: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_key.setter
    def unique_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgsDict(
    TypedDict
):
    unique_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertiesArgs:
    def __init__(
        __self__, *, unique_key: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_key.setter
    def unique_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataSetOutputColumnArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetOutputColumnArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetPermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetPermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class DataSetPhysicalTableMapArgsDict(TypedDict):
    physical_table_map_id: pulumi.Input[_builtins.str]
    custom_sql: NotRequired[pulumi.Input[DataSetPhysicalTableMapCustomSqlArgsDict]]
    relational_table: NotRequired[
        pulumi.Input[DataSetPhysicalTableMapRelationalTableArgsDict]
    ]
    s3_source: NotRequired[pulumi.Input[DataSetPhysicalTableMapS3SourceArgsDict]]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapArgs:
    def __init__(
        __self__,
        *,
        physical_table_map_id: pulumi.Input[_builtins.str],
        custom_sql: Optional[pulumi.Input[DataSetPhysicalTableMapCustomSqlArgs]] = ...,
        relational_table: Optional[
            pulumi.Input[DataSetPhysicalTableMapRelationalTableArgs]
        ] = ...,
        s3_source: Optional[pulumi.Input[DataSetPhysicalTableMapS3SourceArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableMapId")
    def physical_table_map_id(self) -> pulumi.Input[_builtins.str]: ...
    @physical_table_map_id.setter
    def physical_table_map_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="customSql")
    def custom_sql(
        self,
    ) -> Optional[pulumi.Input[DataSetPhysicalTableMapCustomSqlArgs]]: ...
    @custom_sql.setter
    def custom_sql(
        self, value: Optional[pulumi.Input[DataSetPhysicalTableMapCustomSqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="relationalTable")
    def relational_table(
        self,
    ) -> Optional[pulumi.Input[DataSetPhysicalTableMapRelationalTableArgs]]: ...
    @relational_table.setter
    def relational_table(
        self, value: Optional[pulumi.Input[DataSetPhysicalTableMapRelationalTableArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="s3Source")
    def s3_source(
        self,
    ) -> Optional[pulumi.Input[DataSetPhysicalTableMapS3SourceArgs]]: ...
    @s3_source.setter
    def s3_source(
        self, value: Optional[pulumi.Input[DataSetPhysicalTableMapS3SourceArgs]]
    ): ...

class DataSetPhysicalTableMapCustomSqlArgsDict(TypedDict):
    data_source_arn: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    sql_query: pulumi.Input[_builtins.str]
    columns: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DataSetPhysicalTableMapCustomSqlColumnArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapCustomSqlArgs:
    def __init__(
        __self__,
        *,
        data_source_arn: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        sql_query: pulumi.Input[_builtins.str],
        columns: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataSetPhysicalTableMapCustomSqlColumnArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_arn.setter
    def data_source_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="sqlQuery")
    def sql_query(self) -> pulumi.Input[_builtins.str]: ...
    @sql_query.setter
    def sql_query(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[DataSetPhysicalTableMapCustomSqlColumnArgs]]]
    ]: ...
    @columns.setter
    def columns(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataSetPhysicalTableMapCustomSqlColumnArgs]]
            ]
        ],
    ): ...

class DataSetPhysicalTableMapCustomSqlColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapCustomSqlColumnArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class DataSetPhysicalTableMapRelationalTableArgsDict(TypedDict):
    data_source_arn: pulumi.Input[_builtins.str]
    input_columns: pulumi.Input[
        Sequence[
            pulumi.Input[DataSetPhysicalTableMapRelationalTableInputColumnArgsDict]
        ]
    ]
    name: pulumi.Input[_builtins.str]
    catalog: NotRequired[pulumi.Input[_builtins.str]]
    schema: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapRelationalTableArgs:
    def __init__(
        __self__,
        *,
        data_source_arn: pulumi.Input[_builtins.str],
        input_columns: pulumi.Input[
            Sequence[
                pulumi.Input[DataSetPhysicalTableMapRelationalTableInputColumnArgs]
            ]
        ],
        name: pulumi.Input[_builtins.str],
        catalog: Optional[pulumi.Input[_builtins.str]] = ...,
        schema: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_arn.setter
    def data_source_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[DataSetPhysicalTableMapRelationalTableInputColumnArgs]]
    ]: ...
    @input_columns.setter
    def input_columns(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[DataSetPhysicalTableMapRelationalTableInputColumnArgs]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @catalog.setter
    def catalog(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema.setter
    def schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetPhysicalTableMapRelationalTableInputColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapRelationalTableInputColumnArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class DataSetPhysicalTableMapS3SourceArgsDict(TypedDict):
    data_source_arn: pulumi.Input[_builtins.str]
    input_columns: pulumi.Input[
        Sequence[pulumi.Input[DataSetPhysicalTableMapS3SourceInputColumnArgsDict]]
    ]
    upload_settings: pulumi.Input[DataSetPhysicalTableMapS3SourceUploadSettingsArgsDict]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapS3SourceArgs:
    def __init__(
        __self__,
        *,
        data_source_arn: pulumi.Input[_builtins.str],
        input_columns: pulumi.Input[
            Sequence[pulumi.Input[DataSetPhysicalTableMapS3SourceInputColumnArgs]]
        ],
        upload_settings: pulumi.Input[
            DataSetPhysicalTableMapS3SourceUploadSettingsArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_source_arn.setter
    def data_source_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[DataSetPhysicalTableMapS3SourceInputColumnArgs]]
    ]: ...
    @input_columns.setter
    def input_columns(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[DataSetPhysicalTableMapS3SourceInputColumnArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="uploadSettings")
    def upload_settings(
        self,
    ) -> pulumi.Input[DataSetPhysicalTableMapS3SourceUploadSettingsArgs]: ...
    @upload_settings.setter
    def upload_settings(
        self, value: pulumi.Input[DataSetPhysicalTableMapS3SourceUploadSettingsArgs]
    ): ...

class DataSetPhysicalTableMapS3SourceInputColumnArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapS3SourceInputColumnArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...

class DataSetPhysicalTableMapS3SourceUploadSettingsArgsDict(TypedDict):
    contains_header: NotRequired[pulumi.Input[_builtins.bool]]
    delimiter: NotRequired[pulumi.Input[_builtins.str]]
    format: NotRequired[pulumi.Input[_builtins.str]]
    start_from_row: NotRequired[pulumi.Input[_builtins.int]]
    text_qualifier: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetPhysicalTableMapS3SourceUploadSettingsArgs:
    def __init__(
        __self__,
        *,
        contains_header: Optional[pulumi.Input[_builtins.bool]] = ...,
        delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        start_from_row: Optional[pulumi.Input[_builtins.int]] = ...,
        text_qualifier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containsHeader")
    def contains_header(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @contains_header.setter
    def contains_header(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delimiter.setter
    def delimiter(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startFromRow")
    def start_from_row(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @start_from_row.setter
    def start_from_row(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="textQualifier")
    def text_qualifier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text_qualifier.setter
    def text_qualifier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetRefreshPropertiesArgsDict(TypedDict):
    refresh_configuration: pulumi.Input[
        DataSetRefreshPropertiesRefreshConfigurationArgsDict
    ]
    ...

@pulumi.input_type
class DataSetRefreshPropertiesArgs:
    def __init__(
        __self__,
        *,
        refresh_configuration: pulumi.Input[
            DataSetRefreshPropertiesRefreshConfigurationArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="refreshConfiguration")
    def refresh_configuration(
        self,
    ) -> pulumi.Input[DataSetRefreshPropertiesRefreshConfigurationArgs]: ...
    @refresh_configuration.setter
    def refresh_configuration(
        self, value: pulumi.Input[DataSetRefreshPropertiesRefreshConfigurationArgs]
    ): ...

class DataSetRefreshPropertiesRefreshConfigurationArgsDict(TypedDict):
    incremental_refresh: pulumi.Input[
        DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgsDict
    ]
    ...

@pulumi.input_type
class DataSetRefreshPropertiesRefreshConfigurationArgs:
    def __init__(
        __self__,
        *,
        incremental_refresh: pulumi.Input[
            DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="incrementalRefresh")
    def incremental_refresh(
        self,
    ) -> pulumi.Input[
        DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgs
    ]: ...
    @incremental_refresh.setter
    def incremental_refresh(
        self,
        value: pulumi.Input[
            DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgs
        ],
    ): ...

class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgsDict(TypedDict):
    lookback_window: pulumi.Input[
        DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgsDict
    ]
    ...

@pulumi.input_type
class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshArgs:
    def __init__(
        __self__,
        *,
        lookback_window: pulumi.Input[
            DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lookbackWindow")
    def lookback_window(
        self,
    ) -> pulumi.Input[
        DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgs
    ]: ...
    @lookback_window.setter
    def lookback_window(
        self,
        value: pulumi.Input[
            DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgs
        ],
    ): ...

class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgsDict(
    TypedDict
):
    column_name: pulumi.Input[_builtins.str]
    size: pulumi.Input[_builtins.int]
    size_unit: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindowArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        size: pulumi.Input[_builtins.int],
        size_unit: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> pulumi.Input[_builtins.int]: ...
    @size.setter
    def size(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="sizeUnit")
    def size_unit(self) -> pulumi.Input[_builtins.str]: ...
    @size_unit.setter
    def size_unit(self, value: pulumi.Input[_builtins.str]): ...

class DataSetRowLevelPermissionDataSetArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    permission_policy: pulumi.Input[_builtins.str]
    format_version: NotRequired[pulumi.Input[_builtins.str]]
    namespace: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetRowLevelPermissionDataSetArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        permission_policy: pulumi.Input[_builtins.str],
        format_version: Optional[pulumi.Input[_builtins.str]] = ...,
        namespace: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="permissionPolicy")
    def permission_policy(self) -> pulumi.Input[_builtins.str]: ...
    @permission_policy.setter
    def permission_policy(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="formatVersion")
    def format_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format_version.setter
    def format_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetRowLevelPermissionTagConfigurationArgsDict(TypedDict):
    tag_rules: pulumi.Input[
        Sequence[pulumi.Input[DataSetRowLevelPermissionTagConfigurationTagRuleArgsDict]]
    ]
    status: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetRowLevelPermissionTagConfigurationArgs:
    def __init__(
        __self__,
        *,
        tag_rules: pulumi.Input[
            Sequence[pulumi.Input[DataSetRowLevelPermissionTagConfigurationTagRuleArgs]]
        ],
        status: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[DataSetRowLevelPermissionTagConfigurationTagRuleArgs]]
    ]: ...
    @tag_rules.setter
    def tag_rules(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[DataSetRowLevelPermissionTagConfigurationTagRuleArgs]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSetRowLevelPermissionTagConfigurationTagRuleArgsDict(TypedDict):
    column_name: pulumi.Input[_builtins.str]
    tag_key: pulumi.Input[_builtins.str]
    match_all_value: NotRequired[pulumi.Input[_builtins.str]]
    tag_multi_value_delimiter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSetRowLevelPermissionTagConfigurationTagRuleArgs:
    def __init__(
        __self__,
        *,
        column_name: pulumi.Input[_builtins.str],
        tag_key: pulumi.Input[_builtins.str],
        match_all_value: Optional[pulumi.Input[_builtins.str]] = ...,
        tag_multi_value_delimiter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> pulumi.Input[_builtins.str]: ...
    @column_name.setter
    def column_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> pulumi.Input[_builtins.str]: ...
    @tag_key.setter
    def tag_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="matchAllValue")
    def match_all_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_all_value.setter
    def match_all_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tagMultiValueDelimiter")
    def tag_multi_value_delimiter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag_multi_value_delimiter.setter
    def tag_multi_value_delimiter(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class DataSourceCredentialsArgsDict(TypedDict):
    copy_source_arn: NotRequired[pulumi.Input[_builtins.str]]
    credential_pair: NotRequired[
        pulumi.Input[DataSourceCredentialsCredentialPairArgsDict]
    ]
    secret_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSourceCredentialsArgs:
    def __init__(
        __self__,
        *,
        copy_source_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        credential_pair: Optional[
            pulumi.Input[DataSourceCredentialsCredentialPairArgs]
        ] = ...,
        secret_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copySourceArn")
    def copy_source_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @copy_source_arn.setter
    def copy_source_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="credentialPair")
    def credential_pair(
        self,
    ) -> Optional[pulumi.Input[DataSourceCredentialsCredentialPairArgs]]: ...
    @credential_pair.setter
    def credential_pair(
        self, value: Optional[pulumi.Input[DataSourceCredentialsCredentialPairArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secret_arn.setter
    def secret_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceCredentialsCredentialPairArgsDict(TypedDict):
    password: pulumi.Input[_builtins.str]
    username: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceCredentialsCredentialPairArgs:
    def __init__(
        __self__,
        *,
        password: pulumi.Input[_builtins.str],
        username: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> pulumi.Input[_builtins.str]: ...
    @password.setter
    def password(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> pulumi.Input[_builtins.str]: ...
    @username.setter
    def username(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersArgsDict(TypedDict):
    amazon_elasticsearch: NotRequired[
        pulumi.Input[DataSourceParametersAmazonElasticsearchArgsDict]
    ]
    athena: NotRequired[pulumi.Input[DataSourceParametersAthenaArgsDict]]
    aurora: NotRequired[pulumi.Input[DataSourceParametersAuroraArgsDict]]
    aurora_postgresql: NotRequired[
        pulumi.Input[DataSourceParametersAuroraPostgresqlArgsDict]
    ]
    aws_iot_analytics: NotRequired[
        pulumi.Input[DataSourceParametersAwsIotAnalyticsArgsDict]
    ]
    databricks: NotRequired[pulumi.Input[DataSourceParametersDatabricksArgsDict]]
    jira: NotRequired[pulumi.Input[DataSourceParametersJiraArgsDict]]
    maria_db: NotRequired[pulumi.Input[DataSourceParametersMariaDbArgsDict]]
    mysql: NotRequired[pulumi.Input[DataSourceParametersMysqlArgsDict]]
    oracle: NotRequired[pulumi.Input[DataSourceParametersOracleArgsDict]]
    postgresql: NotRequired[pulumi.Input[DataSourceParametersPostgresqlArgsDict]]
    presto: NotRequired[pulumi.Input[DataSourceParametersPrestoArgsDict]]
    rds: NotRequired[pulumi.Input[DataSourceParametersRdsArgsDict]]
    redshift: NotRequired[pulumi.Input[DataSourceParametersRedshiftArgsDict]]
    s3: NotRequired[pulumi.Input[DataSourceParametersS3ArgsDict]]
    service_now: NotRequired[pulumi.Input[DataSourceParametersServiceNowArgsDict]]
    snowflake: NotRequired[pulumi.Input[DataSourceParametersSnowflakeArgsDict]]
    spark: NotRequired[pulumi.Input[DataSourceParametersSparkArgsDict]]
    sql_server: NotRequired[pulumi.Input[DataSourceParametersSqlServerArgsDict]]
    teradata: NotRequired[pulumi.Input[DataSourceParametersTeradataArgsDict]]
    twitter: NotRequired[pulumi.Input[DataSourceParametersTwitterArgsDict]]
    ...

@pulumi.input_type
class DataSourceParametersArgs:
    def __init__(
        __self__,
        *,
        amazon_elasticsearch: Optional[
            pulumi.Input[DataSourceParametersAmazonElasticsearchArgs]
        ] = ...,
        athena: Optional[pulumi.Input[DataSourceParametersAthenaArgs]] = ...,
        aurora: Optional[pulumi.Input[DataSourceParametersAuroraArgs]] = ...,
        aurora_postgresql: Optional[
            pulumi.Input[DataSourceParametersAuroraPostgresqlArgs]
        ] = ...,
        aws_iot_analytics: Optional[
            pulumi.Input[DataSourceParametersAwsIotAnalyticsArgs]
        ] = ...,
        databricks: Optional[pulumi.Input[DataSourceParametersDatabricksArgs]] = ...,
        jira: Optional[pulumi.Input[DataSourceParametersJiraArgs]] = ...,
        maria_db: Optional[pulumi.Input[DataSourceParametersMariaDbArgs]] = ...,
        mysql: Optional[pulumi.Input[DataSourceParametersMysqlArgs]] = ...,
        oracle: Optional[pulumi.Input[DataSourceParametersOracleArgs]] = ...,
        postgresql: Optional[pulumi.Input[DataSourceParametersPostgresqlArgs]] = ...,
        presto: Optional[pulumi.Input[DataSourceParametersPrestoArgs]] = ...,
        rds: Optional[pulumi.Input[DataSourceParametersRdsArgs]] = ...,
        redshift: Optional[pulumi.Input[DataSourceParametersRedshiftArgs]] = ...,
        s3: Optional[pulumi.Input[DataSourceParametersS3Args]] = ...,
        service_now: Optional[pulumi.Input[DataSourceParametersServiceNowArgs]] = ...,
        snowflake: Optional[pulumi.Input[DataSourceParametersSnowflakeArgs]] = ...,
        spark: Optional[pulumi.Input[DataSourceParametersSparkArgs]] = ...,
        sql_server: Optional[pulumi.Input[DataSourceParametersSqlServerArgs]] = ...,
        teradata: Optional[pulumi.Input[DataSourceParametersTeradataArgs]] = ...,
        twitter: Optional[pulumi.Input[DataSourceParametersTwitterArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonElasticsearch")
    def amazon_elasticsearch(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersAmazonElasticsearchArgs]]: ...
    @amazon_elasticsearch.setter
    def amazon_elasticsearch(
        self, value: Optional[pulumi.Input[DataSourceParametersAmazonElasticsearchArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def athena(self) -> Optional[pulumi.Input[DataSourceParametersAthenaArgs]]: ...
    @athena.setter
    def athena(self, value: Optional[pulumi.Input[DataSourceParametersAthenaArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def aurora(self) -> Optional[pulumi.Input[DataSourceParametersAuroraArgs]]: ...
    @aurora.setter
    def aurora(self, value: Optional[pulumi.Input[DataSourceParametersAuroraArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="auroraPostgresql")
    def aurora_postgresql(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersAuroraPostgresqlArgs]]: ...
    @aurora_postgresql.setter
    def aurora_postgresql(
        self, value: Optional[pulumi.Input[DataSourceParametersAuroraPostgresqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="awsIotAnalytics")
    def aws_iot_analytics(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersAwsIotAnalyticsArgs]]: ...
    @aws_iot_analytics.setter
    def aws_iot_analytics(
        self, value: Optional[pulumi.Input[DataSourceParametersAwsIotAnalyticsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def databricks(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersDatabricksArgs]]: ...
    @databricks.setter
    def databricks(
        self, value: Optional[pulumi.Input[DataSourceParametersDatabricksArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def jira(self) -> Optional[pulumi.Input[DataSourceParametersJiraArgs]]: ...
    @jira.setter
    def jira(self, value: Optional[pulumi.Input[DataSourceParametersJiraArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="mariaDb")
    def maria_db(self) -> Optional[pulumi.Input[DataSourceParametersMariaDbArgs]]: ...
    @maria_db.setter
    def maria_db(
        self, value: Optional[pulumi.Input[DataSourceParametersMariaDbArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def mysql(self) -> Optional[pulumi.Input[DataSourceParametersMysqlArgs]]: ...
    @mysql.setter
    def mysql(self, value: Optional[pulumi.Input[DataSourceParametersMysqlArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def oracle(self) -> Optional[pulumi.Input[DataSourceParametersOracleArgs]]: ...
    @oracle.setter
    def oracle(self, value: Optional[pulumi.Input[DataSourceParametersOracleArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def postgresql(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersPostgresqlArgs]]: ...
    @postgresql.setter
    def postgresql(
        self, value: Optional[pulumi.Input[DataSourceParametersPostgresqlArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def presto(self) -> Optional[pulumi.Input[DataSourceParametersPrestoArgs]]: ...
    @presto.setter
    def presto(self, value: Optional[pulumi.Input[DataSourceParametersPrestoArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def rds(self) -> Optional[pulumi.Input[DataSourceParametersRdsArgs]]: ...
    @rds.setter
    def rds(self, value: Optional[pulumi.Input[DataSourceParametersRdsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[pulumi.Input[DataSourceParametersRedshiftArgs]]: ...
    @redshift.setter
    def redshift(
        self, value: Optional[pulumi.Input[DataSourceParametersRedshiftArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[pulumi.Input[DataSourceParametersS3Args]]: ...
    @s3.setter
    def s3(self, value: Optional[pulumi.Input[DataSourceParametersS3Args]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersServiceNowArgs]]: ...
    @service_now.setter
    def service_now(
        self, value: Optional[pulumi.Input[DataSourceParametersServiceNowArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def snowflake(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersSnowflakeArgs]]: ...
    @snowflake.setter
    def snowflake(
        self, value: Optional[pulumi.Input[DataSourceParametersSnowflakeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[pulumi.Input[DataSourceParametersSparkArgs]]: ...
    @spark.setter
    def spark(self, value: Optional[pulumi.Input[DataSourceParametersSparkArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="sqlServer")
    def sql_server(
        self,
    ) -> Optional[pulumi.Input[DataSourceParametersSqlServerArgs]]: ...
    @sql_server.setter
    def sql_server(
        self, value: Optional[pulumi.Input[DataSourceParametersSqlServerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def teradata(self) -> Optional[pulumi.Input[DataSourceParametersTeradataArgs]]: ...
    @teradata.setter
    def teradata(
        self, value: Optional[pulumi.Input[DataSourceParametersTeradataArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def twitter(self) -> Optional[pulumi.Input[DataSourceParametersTwitterArgs]]: ...
    @twitter.setter
    def twitter(
        self, value: Optional[pulumi.Input[DataSourceParametersTwitterArgs]]
    ): ...

class DataSourceParametersAmazonElasticsearchArgsDict(TypedDict):
    domain: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersAmazonElasticsearchArgs:
    def __init__(__self__, *, domain: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> pulumi.Input[_builtins.str]: ...
    @domain.setter
    def domain(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersAthenaArgsDict(TypedDict):
    work_group: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSourceParametersAthenaArgs:
    def __init__(
        __self__, *, work_group: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workGroup")
    def work_group(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @work_group.setter
    def work_group(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceParametersAuroraArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersAuroraArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersAuroraPostgresqlArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersAuroraPostgresqlArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersAwsIotAnalyticsArgsDict(TypedDict):
    data_set_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersAwsIotAnalyticsArgs:
    def __init__(__self__, *, data_set_name: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetName")
    def data_set_name(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_name.setter
    def data_set_name(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersDatabricksArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    sql_endpoint_path: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersDatabricksArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
        sql_endpoint_path: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="sqlEndpointPath")
    def sql_endpoint_path(self) -> pulumi.Input[_builtins.str]: ...
    @sql_endpoint_path.setter
    def sql_endpoint_path(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersJiraArgsDict(TypedDict):
    site_base_url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersJiraArgs:
    def __init__(__self__, *, site_base_url: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteBaseUrl")
    def site_base_url(self) -> pulumi.Input[_builtins.str]: ...
    @site_base_url.setter
    def site_base_url(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersMariaDbArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersMariaDbArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersMysqlArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersMysqlArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersOracleArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersOracleArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersPostgresqlArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersPostgresqlArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersPrestoArgsDict(TypedDict):
    catalog: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersPrestoArgs:
    def __init__(
        __self__,
        *,
        catalog: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> pulumi.Input[_builtins.str]: ...
    @catalog.setter
    def catalog(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersRdsArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    instance_id: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersRdsArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        instance_id: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[_builtins.str]: ...
    @instance_id.setter
    def instance_id(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersRedshiftArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    cluster_id: NotRequired[pulumi.Input[_builtins.str]]
    host: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class DataSourceParametersRedshiftArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        cluster_id: Optional[pulumi.Input[_builtins.str]] = ...,
        host: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class DataSourceParametersS3ArgsDict(TypedDict):
    manifest_file_location: pulumi.Input[
        DataSourceParametersS3ManifestFileLocationArgsDict
    ]
    role_arn: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DataSourceParametersS3Args:
    def __init__(
        __self__,
        *,
        manifest_file_location: pulumi.Input[
            DataSourceParametersS3ManifestFileLocationArgs
        ],
        role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manifestFileLocation")
    def manifest_file_location(
        self,
    ) -> pulumi.Input[DataSourceParametersS3ManifestFileLocationArgs]: ...
    @manifest_file_location.setter
    def manifest_file_location(
        self, value: pulumi.Input[DataSourceParametersS3ManifestFileLocationArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role_arn.setter
    def role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataSourceParametersS3ManifestFileLocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersS3ManifestFileLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersServiceNowArgsDict(TypedDict):
    site_base_url: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersServiceNowArgs:
    def __init__(__self__, *, site_base_url: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteBaseUrl")
    def site_base_url(self) -> pulumi.Input[_builtins.str]: ...
    @site_base_url.setter
    def site_base_url(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersSnowflakeArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    warehouse: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersSnowflakeArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        warehouse: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def warehouse(self) -> pulumi.Input[_builtins.str]: ...
    @warehouse.setter
    def warehouse(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceParametersSparkArgsDict(TypedDict):
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersSparkArgs:
    def __init__(
        __self__,
        *,
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersSqlServerArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersSqlServerArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersTeradataArgsDict(TypedDict):
    database: pulumi.Input[_builtins.str]
    host: pulumi.Input[_builtins.str]
    port: pulumi.Input[_builtins.int]
    ...

@pulumi.input_type
class DataSourceParametersTeradataArgs:
    def __init__(
        __self__,
        *,
        database: pulumi.Input[_builtins.str],
        host: pulumi.Input[_builtins.str],
        port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> pulumi.Input[_builtins.str]: ...
    @database.setter
    def database(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> pulumi.Input[_builtins.str]: ...
    @host.setter
    def host(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class DataSourceParametersTwitterArgsDict(TypedDict):
    max_rows: pulumi.Input[_builtins.int]
    query: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceParametersTwitterArgs:
    def __init__(
        __self__,
        *,
        max_rows: pulumi.Input[_builtins.int],
        query: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRows")
    def max_rows(self) -> pulumi.Input[_builtins.int]: ...
    @max_rows.setter
    def max_rows(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Input[_builtins.str]: ...
    @query.setter
    def query(self, value: pulumi.Input[_builtins.str]): ...

class DataSourcePermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourcePermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class DataSourceSslPropertiesArgsDict(TypedDict):
    disable_ssl: pulumi.Input[_builtins.bool]
    ...

@pulumi.input_type
class DataSourceSslPropertiesArgs:
    def __init__(__self__, *, disable_ssl: pulumi.Input[_builtins.bool]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableSsl")
    def disable_ssl(self) -> pulumi.Input[_builtins.bool]: ...
    @disable_ssl.setter
    def disable_ssl(self, value: pulumi.Input[_builtins.bool]): ...

class DataSourceVpcConnectionPropertiesArgsDict(TypedDict):
    vpc_connection_arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class DataSourceVpcConnectionPropertiesArgs:
    def __init__(
        __self__, *, vpc_connection_arn: pulumi.Input[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectionArn")
    def vpc_connection_arn(self) -> pulumi.Input[_builtins.str]: ...
    @vpc_connection_arn.setter
    def vpc_connection_arn(self, value: pulumi.Input[_builtins.str]): ...

class FolderPermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class FolderPermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class IamPolicyAssignmentIdentitiesArgsDict(TypedDict):
    groups: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    users: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class IamPolicyAssignmentIdentitiesArgs:
    def __init__(
        __self__,
        *,
        groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        users: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @groups.setter
    def groups(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def users(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @users.setter
    def users(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class KeyRegistrationKeyRegistrationArgsDict(TypedDict):
    key_arn: pulumi.Input[_builtins.str]
    default_key: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class KeyRegistrationKeyRegistrationArgs:
    def __init__(
        __self__,
        *,
        key_arn: pulumi.Input[_builtins.str],
        default_key: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> pulumi.Input[_builtins.str]: ...
    @key_arn.setter
    def key_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultKey")
    def default_key(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @default_key.setter
    def default_key(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class NamespaceTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class NamespaceTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RefreshScheduleScheduleArgsDict(TypedDict):
    refresh_type: pulumi.Input[_builtins.str]
    schedule_frequency: pulumi.Input[RefreshScheduleScheduleScheduleFrequencyArgsDict]
    start_after_date_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RefreshScheduleScheduleArgs:
    def __init__(
        __self__,
        *,
        refresh_type: pulumi.Input[_builtins.str],
        schedule_frequency: pulumi.Input[RefreshScheduleScheduleScheduleFrequencyArgs],
        start_after_date_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="refreshType")
    def refresh_type(self) -> pulumi.Input[_builtins.str]: ...
    @refresh_type.setter
    def refresh_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> pulumi.Input[RefreshScheduleScheduleScheduleFrequencyArgs]: ...
    @schedule_frequency.setter
    def schedule_frequency(
        self, value: pulumi.Input[RefreshScheduleScheduleScheduleFrequencyArgs]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startAfterDateTime")
    def start_after_date_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_after_date_time.setter
    def start_after_date_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RefreshScheduleScheduleScheduleFrequencyArgsDict(TypedDict):
    interval: pulumi.Input[_builtins.str]
    refresh_on_day: NotRequired[
        pulumi.Input[RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgsDict]
    ]
    time_of_the_day: NotRequired[pulumi.Input[_builtins.str]]
    timezone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RefreshScheduleScheduleScheduleFrequencyArgs:
    def __init__(
        __self__,
        *,
        interval: pulumi.Input[_builtins.str],
        refresh_on_day: Optional[
            pulumi.Input[RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgs]
        ] = ...,
        time_of_the_day: Optional[pulumi.Input[_builtins.str]] = ...,
        timezone: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> pulumi.Input[_builtins.str]: ...
    @interval.setter
    def interval(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="refreshOnDay")
    def refresh_on_day(
        self,
    ) -> Optional[
        pulumi.Input[RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgs]
    ]: ...
    @refresh_on_day.setter
    def refresh_on_day(
        self,
        value: Optional[
            pulumi.Input[RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeOfTheDay")
    def time_of_the_day(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_of_the_day.setter
    def time_of_the_day(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgsDict(TypedDict):
    day_of_month: NotRequired[pulumi.Input[_builtins.str]]
    day_of_week: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class RefreshScheduleScheduleScheduleFrequencyRefreshOnDayArgs:
    def __init__(
        __self__,
        *,
        day_of_month: Optional[pulumi.Input[_builtins.str]] = ...,
        day_of_week: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_month.setter
    def day_of_month(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TemplatePermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TemplatePermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class TemplateSourceEntityArgsDict(TypedDict):
    source_analysis: NotRequired[
        pulumi.Input[TemplateSourceEntitySourceAnalysisArgsDict]
    ]
    source_template: NotRequired[
        pulumi.Input[TemplateSourceEntitySourceTemplateArgsDict]
    ]
    ...

@pulumi.input_type
class TemplateSourceEntityArgs:
    def __init__(
        __self__,
        *,
        source_analysis: Optional[
            pulumi.Input[TemplateSourceEntitySourceAnalysisArgs]
        ] = ...,
        source_template: Optional[
            pulumi.Input[TemplateSourceEntitySourceTemplateArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceAnalysis")
    def source_analysis(
        self,
    ) -> Optional[pulumi.Input[TemplateSourceEntitySourceAnalysisArgs]]: ...
    @source_analysis.setter
    def source_analysis(
        self, value: Optional[pulumi.Input[TemplateSourceEntitySourceAnalysisArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[pulumi.Input[TemplateSourceEntitySourceTemplateArgs]]: ...
    @source_template.setter
    def source_template(
        self, value: Optional[pulumi.Input[TemplateSourceEntitySourceTemplateArgs]]
    ): ...

class TemplateSourceEntitySourceAnalysisArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    data_set_references: pulumi.Input[
        Sequence[
            pulumi.Input[TemplateSourceEntitySourceAnalysisDataSetReferenceArgsDict]
        ]
    ]
    ...

@pulumi.input_type
class TemplateSourceEntitySourceAnalysisArgs:
    def __init__(
        __self__,
        *,
        arn: pulumi.Input[_builtins.str],
        data_set_references: pulumi.Input[
            Sequence[
                pulumi.Input[TemplateSourceEntitySourceAnalysisDataSetReferenceArgs]
            ]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[TemplateSourceEntitySourceAnalysisDataSetReferenceArgs]]
    ]: ...
    @data_set_references.setter
    def data_set_references(
        self,
        value: pulumi.Input[
            Sequence[
                pulumi.Input[TemplateSourceEntitySourceAnalysisDataSetReferenceArgs]
            ]
        ],
    ): ...

class TemplateSourceEntitySourceAnalysisDataSetReferenceArgsDict(TypedDict):
    data_set_arn: pulumi.Input[_builtins.str]
    data_set_placeholder: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TemplateSourceEntitySourceAnalysisDataSetReferenceArgs:
    def __init__(
        __self__,
        *,
        data_set_arn: pulumi.Input[_builtins.str],
        data_set_placeholder: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_arn.setter
    def data_set_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> pulumi.Input[_builtins.str]: ...
    @data_set_placeholder.setter
    def data_set_placeholder(self, value: pulumi.Input[_builtins.str]): ...

class TemplateSourceEntitySourceTemplateArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class TemplateSourceEntitySourceTemplateArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]: ...
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): ...

class ThemeConfigurationArgsDict(TypedDict):
    data_color_palette: NotRequired[
        pulumi.Input[ThemeConfigurationDataColorPaletteArgsDict]
    ]
    sheet: NotRequired[pulumi.Input[ThemeConfigurationSheetArgsDict]]
    typography: NotRequired[pulumi.Input[ThemeConfigurationTypographyArgsDict]]
    ui_color_palette: NotRequired[
        pulumi.Input[ThemeConfigurationUiColorPaletteArgsDict]
    ]
    ...

@pulumi.input_type
class ThemeConfigurationArgs:
    def __init__(
        __self__,
        *,
        data_color_palette: Optional[
            pulumi.Input[ThemeConfigurationDataColorPaletteArgs]
        ] = ...,
        sheet: Optional[pulumi.Input[ThemeConfigurationSheetArgs]] = ...,
        typography: Optional[pulumi.Input[ThemeConfigurationTypographyArgs]] = ...,
        ui_color_palette: Optional[
            pulumi.Input[ThemeConfigurationUiColorPaletteArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataColorPalette")
    def data_color_palette(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationDataColorPaletteArgs]]: ...
    @data_color_palette.setter
    def data_color_palette(
        self, value: Optional[pulumi.Input[ThemeConfigurationDataColorPaletteArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def sheet(self) -> Optional[pulumi.Input[ThemeConfigurationSheetArgs]]: ...
    @sheet.setter
    def sheet(self, value: Optional[pulumi.Input[ThemeConfigurationSheetArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def typography(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationTypographyArgs]]: ...
    @typography.setter
    def typography(
        self, value: Optional[pulumi.Input[ThemeConfigurationTypographyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="uiColorPalette")
    def ui_color_palette(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationUiColorPaletteArgs]]: ...
    @ui_color_palette.setter
    def ui_color_palette(
        self, value: Optional[pulumi.Input[ThemeConfigurationUiColorPaletteArgs]]
    ): ...

class ThemeConfigurationDataColorPaletteArgsDict(TypedDict):
    colors: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    empty_fill_color: NotRequired[pulumi.Input[_builtins.str]]
    min_max_gradients: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ThemeConfigurationDataColorPaletteArgs:
    def __init__(
        __self__,
        *,
        colors: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        empty_fill_color: Optional[pulumi.Input[_builtins.str]] = ...,
        min_max_gradients: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def colors(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @colors.setter
    def colors(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emptyFillColor")
    def empty_fill_color(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @empty_fill_color.setter
    def empty_fill_color(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="minMaxGradients")
    def min_max_gradients(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @min_max_gradients.setter
    def min_max_gradients(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ThemeConfigurationSheetArgsDict(TypedDict):
    tile: NotRequired[pulumi.Input[ThemeConfigurationSheetTileArgsDict]]
    tile_layout: NotRequired[pulumi.Input[ThemeConfigurationSheetTileLayoutArgsDict]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetArgs:
    def __init__(
        __self__,
        *,
        tile: Optional[pulumi.Input[ThemeConfigurationSheetTileArgs]] = ...,
        tile_layout: Optional[
            pulumi.Input[ThemeConfigurationSheetTileLayoutArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tile(self) -> Optional[pulumi.Input[ThemeConfigurationSheetTileArgs]]: ...
    @tile.setter
    def tile(self, value: Optional[pulumi.Input[ThemeConfigurationSheetTileArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="tileLayout")
    def tile_layout(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutArgs]]: ...
    @tile_layout.setter
    def tile_layout(
        self, value: Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutArgs]]
    ): ...

class ThemeConfigurationSheetTileArgsDict(TypedDict):
    border: NotRequired[pulumi.Input[ThemeConfigurationSheetTileBorderArgsDict]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetTileArgs:
    def __init__(
        __self__,
        *,
        border: Optional[pulumi.Input[ThemeConfigurationSheetTileBorderArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def border(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationSheetTileBorderArgs]]: ...
    @border.setter
    def border(
        self, value: Optional[pulumi.Input[ThemeConfigurationSheetTileBorderArgs]]
    ): ...

class ThemeConfigurationSheetTileBorderArgsDict(TypedDict):
    show: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetTileBorderArgs:
    def __init__(
        __self__, *, show: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @show.setter
    def show(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ThemeConfigurationSheetTileLayoutArgsDict(TypedDict):
    gutter: NotRequired[pulumi.Input[ThemeConfigurationSheetTileLayoutGutterArgsDict]]
    margin: NotRequired[pulumi.Input[ThemeConfigurationSheetTileLayoutMarginArgsDict]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetTileLayoutArgs:
    def __init__(
        __self__,
        *,
        gutter: Optional[
            pulumi.Input[ThemeConfigurationSheetTileLayoutGutterArgs]
        ] = ...,
        margin: Optional[
            pulumi.Input[ThemeConfigurationSheetTileLayoutMarginArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gutter(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutGutterArgs]]: ...
    @gutter.setter
    def gutter(
        self, value: Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutGutterArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def margin(
        self,
    ) -> Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutMarginArgs]]: ...
    @margin.setter
    def margin(
        self, value: Optional[pulumi.Input[ThemeConfigurationSheetTileLayoutMarginArgs]]
    ): ...

class ThemeConfigurationSheetTileLayoutGutterArgsDict(TypedDict):
    show: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetTileLayoutGutterArgs:
    def __init__(
        __self__, *, show: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @show.setter
    def show(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ThemeConfigurationSheetTileLayoutMarginArgsDict(TypedDict):
    show: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ThemeConfigurationSheetTileLayoutMarginArgs:
    def __init__(
        __self__, *, show: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @show.setter
    def show(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ThemeConfigurationTypographyArgsDict(TypedDict):
    font_families: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ThemeConfigurationTypographyFontFamilyArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class ThemeConfigurationTypographyArgs:
    def __init__(
        __self__,
        *,
        font_families: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ThemeConfigurationTypographyFontFamilyArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamilies")
    def font_families(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ThemeConfigurationTypographyFontFamilyArgs]]]
    ]: ...
    @font_families.setter
    def font_families(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ThemeConfigurationTypographyFontFamilyArgs]]
            ]
        ],
    ): ...

class ThemeConfigurationTypographyFontFamilyArgsDict(TypedDict):
    font_family: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ThemeConfigurationTypographyFontFamilyArgs:
    def __init__(
        __self__, *, font_family: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamily")
    def font_family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @font_family.setter
    def font_family(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThemeConfigurationUiColorPaletteArgsDict(TypedDict):
    accent: NotRequired[pulumi.Input[_builtins.str]]
    accent_foreground: NotRequired[pulumi.Input[_builtins.str]]
    danger: NotRequired[pulumi.Input[_builtins.str]]
    danger_foreground: NotRequired[pulumi.Input[_builtins.str]]
    dimension: NotRequired[pulumi.Input[_builtins.str]]
    dimension_foreground: NotRequired[pulumi.Input[_builtins.str]]
    measure: NotRequired[pulumi.Input[_builtins.str]]
    measure_foreground: NotRequired[pulumi.Input[_builtins.str]]
    primary_background: NotRequired[pulumi.Input[_builtins.str]]
    primary_foreground: NotRequired[pulumi.Input[_builtins.str]]
    secondary_background: NotRequired[pulumi.Input[_builtins.str]]
    secondary_foreground: NotRequired[pulumi.Input[_builtins.str]]
    success: NotRequired[pulumi.Input[_builtins.str]]
    success_foreground: NotRequired[pulumi.Input[_builtins.str]]
    warning: NotRequired[pulumi.Input[_builtins.str]]
    warning_foreground: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ThemeConfigurationUiColorPaletteArgs:
    def __init__(
        __self__,
        *,
        accent: Optional[pulumi.Input[_builtins.str]] = ...,
        accent_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        danger: Optional[pulumi.Input[_builtins.str]] = ...,
        danger_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        dimension: Optional[pulumi.Input[_builtins.str]] = ...,
        dimension_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        measure: Optional[pulumi.Input[_builtins.str]] = ...,
        measure_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_background: Optional[pulumi.Input[_builtins.str]] = ...,
        primary_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_background: Optional[pulumi.Input[_builtins.str]] = ...,
        secondary_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        success: Optional[pulumi.Input[_builtins.str]] = ...,
        success_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
        warning: Optional[pulumi.Input[_builtins.str]] = ...,
        warning_foreground: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accent.setter
    def accent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="accentForeground")
    def accent_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @accent_foreground.setter
    def accent_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def danger(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @danger.setter
    def danger(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dangerForeground")
    def danger_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @danger_foreground.setter
    def danger_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dimension.setter
    def dimension(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dimensionForeground")
    def dimension_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dimension_foreground.setter
    def dimension_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def measure(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @measure.setter
    def measure(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="measureForeground")
    def measure_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @measure_foreground.setter
    def measure_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryBackground")
    def primary_background(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_background.setter
    def primary_background(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="primaryForeground")
    def primary_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @primary_foreground.setter
    def primary_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryBackground")
    def secondary_background(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_background.setter
    def secondary_background(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="secondaryForeground")
    def secondary_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @secondary_foreground.setter
    def secondary_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def success(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success.setter
    def success(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="successForeground")
    def success_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @success_foreground.setter
    def success_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def warning(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warning.setter
    def warning(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="warningForeground")
    def warning_foreground(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @warning_foreground.setter
    def warning_foreground(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ThemePermissionArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    principal: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ThemePermissionArgs:
    def __init__(
        __self__,
        *,
        actions: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        principal: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> pulumi.Input[_builtins.str]: ...
    @principal.setter
    def principal(self, value: pulumi.Input[_builtins.str]): ...

class VpcConnectionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class VpcConnectionTimeoutsArgs:
    def __init__(
        __self__,
        *,
        create: Optional[pulumi.Input[_builtins.str]] = ...,
        delete: Optional[pulumi.Input[_builtins.str]] = ...,
        update: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): ...
