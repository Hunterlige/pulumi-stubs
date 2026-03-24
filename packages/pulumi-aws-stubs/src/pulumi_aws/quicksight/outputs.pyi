import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AccountSettingsTimeouts",
    "AnalysisParameters",
    "AnalysisParametersDateTimeParameter",
    "AnalysisParametersDecimalParameter",
    "AnalysisParametersIntegerParameter",
    "AnalysisParametersStringParameter",
    "AnalysisPermission",
    "AnalysisSourceEntity",
    "AnalysisSourceEntitySourceTemplate",
    "AnalysisSourceEntitySourceTemplateDataSetReference",
    "CustomPermissionsCapabilities",
    "DashboardDashboardPublishOptions",
    ...,
    ...,
    ...,
    ...,
    "DashboardDashboardPublishOptionsExportToCsvOption",
    ...,
    ...,
    ...,
    ...,
    "DashboardDashboardPublishOptionsVisualMenuOption",
    "DashboardParameters",
    "DashboardParametersDateTimeParameter",
    "DashboardParametersDecimalParameter",
    "DashboardParametersIntegerParameter",
    "DashboardParametersStringParameter",
    "DashboardPermission",
    "DashboardSourceEntity",
    "DashboardSourceEntitySourceTemplate",
    ...,
    "DataSetColumnGroup",
    "DataSetColumnGroupGeoSpatialColumnGroup",
    "DataSetColumnLevelPermissionRule",
    "DataSetDataSetUsageConfiguration",
    "DataSetFieldFolder",
    "DataSetLogicalTableMap",
    "DataSetLogicalTableMapDataTransform",
    ...,
    ...,
    ...,
    "DataSetLogicalTableMapDataTransformFilterOperation",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "DataSetLogicalTableMapSource",
    "DataSetLogicalTableMapSourceJoinInstruction",
    ...,
    ...,
    "DataSetOutputColumn",
    "DataSetPermission",
    "DataSetPhysicalTableMap",
    "DataSetPhysicalTableMapCustomSql",
    "DataSetPhysicalTableMapCustomSqlColumn",
    "DataSetPhysicalTableMapRelationalTable",
    "DataSetPhysicalTableMapRelationalTableInputColumn",
    "DataSetPhysicalTableMapS3Source",
    "DataSetPhysicalTableMapS3SourceInputColumn",
    "DataSetPhysicalTableMapS3SourceUploadSettings",
    "DataSetRefreshProperties",
    "DataSetRefreshPropertiesRefreshConfiguration",
    ...,
    ...,
    "DataSetRowLevelPermissionDataSet",
    "DataSetRowLevelPermissionTagConfiguration",
    "DataSetRowLevelPermissionTagConfigurationTagRule",
    "DataSourceCredentials",
    "DataSourceCredentialsCredentialPair",
    "DataSourceParameters",
    "DataSourceParametersAmazonElasticsearch",
    "DataSourceParametersAthena",
    "DataSourceParametersAurora",
    "DataSourceParametersAuroraPostgresql",
    "DataSourceParametersAwsIotAnalytics",
    "DataSourceParametersDatabricks",
    "DataSourceParametersJira",
    "DataSourceParametersMariaDb",
    "DataSourceParametersMysql",
    "DataSourceParametersOracle",
    "DataSourceParametersPostgresql",
    "DataSourceParametersPresto",
    "DataSourceParametersRds",
    "DataSourceParametersRedshift",
    "DataSourceParametersS3",
    "DataSourceParametersS3ManifestFileLocation",
    "DataSourceParametersServiceNow",
    "DataSourceParametersSnowflake",
    "DataSourceParametersSpark",
    "DataSourceParametersSqlServer",
    "DataSourceParametersTeradata",
    "DataSourceParametersTwitter",
    "DataSourcePermission",
    "DataSourceSslProperties",
    "DataSourceVpcConnectionProperties",
    "FolderPermission",
    "IamPolicyAssignmentIdentities",
    "KeyRegistrationKeyRegistration",
    "NamespaceTimeouts",
    "RefreshScheduleSchedule",
    "RefreshScheduleScheduleScheduleFrequency",
    ...,
    "TemplatePermission",
    "TemplateSourceEntity",
    "TemplateSourceEntitySourceAnalysis",
    "TemplateSourceEntitySourceAnalysisDataSetReference",
    "TemplateSourceEntitySourceTemplate",
    "ThemeConfiguration",
    "ThemeConfigurationDataColorPalette",
    "ThemeConfigurationSheet",
    "ThemeConfigurationSheetTile",
    "ThemeConfigurationSheetTileBorder",
    "ThemeConfigurationSheetTileLayout",
    "ThemeConfigurationSheetTileLayoutGutter",
    "ThemeConfigurationSheetTileLayoutMargin",
    "ThemeConfigurationTypography",
    "ThemeConfigurationTypographyFontFamily",
    "ThemeConfigurationUiColorPalette",
    "ThemePermission",
    "VpcConnectionTimeouts",
    "GetDataSetColumnGroupResult",
    "GetDataSetColumnGroupGeoSpatialColumnGroupResult",
    "GetDataSetColumnLevelPermissionRuleResult",
    "GetDataSetDataSetUsageConfigurationResult",
    "GetDataSetFieldFolderResult",
    "GetDataSetLogicalTableMapResult",
    "GetDataSetLogicalTableMapDataTransformResult",
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
    "GetDataSetLogicalTableMapSourceResult",
    ...,
    ...,
    ...,
    "GetDataSetPermissionResult",
    "GetDataSetPhysicalTableMapResult",
    "GetDataSetPhysicalTableMapCustomSqlResult",
    "GetDataSetPhysicalTableMapCustomSqlColumnResult",
    "GetDataSetPhysicalTableMapRelationalTableResult",
    ...,
    "GetDataSetPhysicalTableMapS3SourceResult",
    ...,
    ...,
    "GetDataSetRowLevelPermissionDataSetResult",
    "GetDataSetRowLevelPermissionTagConfigurationResult",
    ...,
    "GetQuicksightAnalysisPermissionResult",
    "GetThemeConfigurationResult",
    "GetThemeConfigurationDataColorPaletteResult",
    "GetThemeConfigurationSheetResult",
    "GetThemeConfigurationSheetTileResult",
    "GetThemeConfigurationSheetTileBorderResult",
    "GetThemeConfigurationSheetTileLayoutResult",
    "GetThemeConfigurationSheetTileLayoutGutterResult",
    "GetThemeConfigurationSheetTileLayoutMarginResult",
    "GetThemeConfigurationTypographyResult",
    "GetThemeConfigurationTypographyFontFamilyResult",
    "GetThemeConfigurationUiColorPaletteResult",
    "GetThemePermissionResult",
]

@pulumi.output_type
class AccountSettingsTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AnalysisParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_time_parameters: Optional[
            Sequence[outputs.AnalysisParametersDateTimeParameter]
        ] = ...,
        decimal_parameters: Optional[
            Sequence[outputs.AnalysisParametersDecimalParameter]
        ] = ...,
        integer_parameters: Optional[
            Sequence[outputs.AnalysisParametersIntegerParameter]
        ] = ...,
        string_parameters: Optional[
            Sequence[outputs.AnalysisParametersStringParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeParameters")
    def date_time_parameters(
        self,
    ) -> Optional[Sequence[outputs.AnalysisParametersDateTimeParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="decimalParameters")
    def decimal_parameters(
        self,
    ) -> Optional[Sequence[outputs.AnalysisParametersDecimalParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="integerParameters")
    def integer_parameters(
        self,
    ) -> Optional[Sequence[outputs.AnalysisParametersIntegerParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="stringParameters")
    def string_parameters(
        self,
    ) -> Optional[Sequence[outputs.AnalysisParametersStringParameter]]: ...

@pulumi.output_type
class AnalysisParametersDateTimeParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AnalysisParametersDecimalParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.float]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.float]: ...

@pulumi.output_type
class AnalysisParametersIntegerParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class AnalysisParametersStringParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class AnalysisPermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class AnalysisSourceEntity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_template: Optional[outputs.AnalysisSourceEntitySourceTemplate] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[outputs.AnalysisSourceEntitySourceTemplate]: ...

@pulumi.output_type
class AnalysisSourceEntitySourceTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        data_set_references: Sequence[
            outputs.AnalysisSourceEntitySourceTemplateDataSetReference
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> Sequence[outputs.AnalysisSourceEntitySourceTemplateDataSetReference]: ...

@pulumi.output_type
class AnalysisSourceEntitySourceTemplateDataSetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_set_arn: _builtins.str, data_set_placeholder: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> _builtins.str: ...

@pulumi.output_type
class CustomPermissionsCapabilities(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        add_or_run_anomaly_detection_for_analyses: Optional[_builtins.str] = ...,
        create_and_update_dashboard_email_reports: Optional[_builtins.str] = ...,
        create_and_update_data_sources: Optional[_builtins.str] = ...,
        create_and_update_datasets: Optional[_builtins.str] = ...,
        create_and_update_themes: Optional[_builtins.str] = ...,
        create_and_update_threshold_alerts: Optional[_builtins.str] = ...,
        create_shared_folders: Optional[_builtins.str] = ...,
        create_spice_dataset: Optional[_builtins.str] = ...,
        export_to_csv: Optional[_builtins.str] = ...,
        export_to_csv_in_scheduled_reports: Optional[_builtins.str] = ...,
        export_to_excel: Optional[_builtins.str] = ...,
        export_to_excel_in_scheduled_reports: Optional[_builtins.str] = ...,
        export_to_pdf: Optional[_builtins.str] = ...,
        export_to_pdf_in_scheduled_reports: Optional[_builtins.str] = ...,
        include_content_in_scheduled_reports_email: Optional[_builtins.str] = ...,
        print_reports: Optional[_builtins.str] = ...,
        rename_shared_folders: Optional[_builtins.str] = ...,
        share_analyses: Optional[_builtins.str] = ...,
        share_dashboards: Optional[_builtins.str] = ...,
        share_data_sources: Optional[_builtins.str] = ...,
        share_datasets: Optional[_builtins.str] = ...,
        subscribe_dashboard_email_reports: Optional[_builtins.str] = ...,
        view_account_spice_capacity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="addOrRunAnomalyDetectionForAnalyses")
    def add_or_run_anomaly_detection_for_analyses(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDashboardEmailReports")
    def create_and_update_dashboard_email_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDataSources")
    def create_and_update_data_sources(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateDatasets")
    def create_and_update_datasets(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateThemes")
    def create_and_update_themes(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createAndUpdateThresholdAlerts")
    def create_and_update_threshold_alerts(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createSharedFolders")
    def create_shared_folders(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createSpiceDataset")
    def create_spice_dataset(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToCsv")
    def export_to_csv(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToCsvInScheduledReports")
    def export_to_csv_in_scheduled_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToExcel")
    def export_to_excel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToExcelInScheduledReports")
    def export_to_excel_in_scheduled_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToPdf")
    def export_to_pdf(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="exportToPdfInScheduledReports")
    def export_to_pdf_in_scheduled_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="includeContentInScheduledReportsEmail")
    def include_content_in_scheduled_reports_email(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="printReports")
    def print_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="renameSharedFolders")
    def rename_shared_folders(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareAnalyses")
    def share_analyses(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareDashboards")
    def share_dashboards(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareDataSources")
    def share_data_sources(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="shareDatasets")
    def share_datasets(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subscribeDashboardEmailReports")
    def subscribe_dashboard_email_reports(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="viewAccountSpiceCapacity")
    def view_account_spice_capacity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptions(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ad_hoc_filtering_option: Optional[
            outputs.DashboardDashboardPublishOptionsAdHocFilteringOption
        ] = ...,
        data_point_drill_up_down_option: Optional[
            outputs.DashboardDashboardPublishOptionsDataPointDrillUpDownOption
        ] = ...,
        data_point_menu_label_option: Optional[
            outputs.DashboardDashboardPublishOptionsDataPointMenuLabelOption
        ] = ...,
        data_point_tooltip_option: Optional[
            outputs.DashboardDashboardPublishOptionsDataPointTooltipOption
        ] = ...,
        export_to_csv_option: Optional[
            outputs.DashboardDashboardPublishOptionsExportToCsvOption
        ] = ...,
        export_with_hidden_fields_option: Optional[
            outputs.DashboardDashboardPublishOptionsExportWithHiddenFieldsOption
        ] = ...,
        sheet_controls_option: Optional[
            outputs.DashboardDashboardPublishOptionsSheetControlsOption
        ] = ...,
        sheet_layout_element_maximization_option: Optional[
            outputs.DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOption
        ] = ...,
        visual_axis_sort_option: Optional[
            outputs.DashboardDashboardPublishOptionsVisualAxisSortOption
        ] = ...,
        visual_menu_option: Optional[
            outputs.DashboardDashboardPublishOptionsVisualMenuOption
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="adHocFilteringOption")
    def ad_hoc_filtering_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsAdHocFilteringOption]: ...
    @_builtins.property
    @pulumi.getter(name="dataPointDrillUpDownOption")
    def data_point_drill_up_down_option(
        self,
    ) -> Optional[
        outputs.DashboardDashboardPublishOptionsDataPointDrillUpDownOption
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dataPointMenuLabelOption")
    def data_point_menu_label_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsDataPointMenuLabelOption]: ...
    @_builtins.property
    @pulumi.getter(name="dataPointTooltipOption")
    def data_point_tooltip_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsDataPointTooltipOption]: ...
    @_builtins.property
    @pulumi.getter(name="exportToCsvOption")
    def export_to_csv_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsExportToCsvOption]: ...
    @_builtins.property
    @pulumi.getter(name="exportWithHiddenFieldsOption")
    def export_with_hidden_fields_option(
        self,
    ) -> Optional[
        outputs.DashboardDashboardPublishOptionsExportWithHiddenFieldsOption
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sheetControlsOption")
    def sheet_controls_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsSheetControlsOption]: ...
    @_builtins.property
    @pulumi.getter(name="sheetLayoutElementMaximizationOption")
    def sheet_layout_element_maximization_option(
        self,
    ) -> Optional[
        outputs.DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOption
    ]: ...
    @_builtins.property
    @pulumi.getter(name="visualAxisSortOption")
    def visual_axis_sort_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsVisualAxisSortOption]: ...
    @_builtins.property
    @pulumi.getter(name="visualMenuOption")
    def visual_menu_option(
        self,
    ) -> Optional[outputs.DashboardDashboardPublishOptionsVisualMenuOption]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsAdHocFilteringOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsDataPointDrillUpDownOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsDataPointMenuLabelOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsDataPointTooltipOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsExportToCsvOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsExportWithHiddenFieldsOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsSheetControlsOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, visibility_state: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="visibilityState")
    def visibility_state(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsSheetLayoutElementMaximizationOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsVisualAxisSortOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardDashboardPublishOptionsVisualMenuOption(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, availability_status: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="availabilityStatus")
    def availability_status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DashboardParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        date_time_parameters: Optional[
            Sequence[outputs.DashboardParametersDateTimeParameter]
        ] = ...,
        decimal_parameters: Optional[
            Sequence[outputs.DashboardParametersDecimalParameter]
        ] = ...,
        integer_parameters: Optional[
            Sequence[outputs.DashboardParametersIntegerParameter]
        ] = ...,
        string_parameters: Optional[
            Sequence[outputs.DashboardParametersStringParameter]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dateTimeParameters")
    def date_time_parameters(
        self,
    ) -> Optional[Sequence[outputs.DashboardParametersDateTimeParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="decimalParameters")
    def decimal_parameters(
        self,
    ) -> Optional[Sequence[outputs.DashboardParametersDecimalParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="integerParameters")
    def integer_parameters(
        self,
    ) -> Optional[Sequence[outputs.DashboardParametersIntegerParameter]]: ...
    @_builtins.property
    @pulumi.getter(name="stringParameters")
    def string_parameters(
        self,
    ) -> Optional[Sequence[outputs.DashboardParametersStringParameter]]: ...

@pulumi.output_type
class DashboardParametersDateTimeParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DashboardParametersDecimalParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.float]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.float]: ...

@pulumi.output_type
class DashboardParametersIntegerParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.int]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.int]: ...

@pulumi.output_type
class DashboardParametersStringParameter(dict):
    def __init__(
        __self__, *, name: _builtins.str, values: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def values(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DashboardPermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class DashboardSourceEntity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_template: Optional[outputs.DashboardSourceEntitySourceTemplate] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[outputs.DashboardSourceEntitySourceTemplate]: ...

@pulumi.output_type
class DashboardSourceEntitySourceTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        data_set_references: Sequence[
            outputs.DashboardSourceEntitySourceTemplateDataSetReference
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> Sequence[outputs.DashboardSourceEntitySourceTemplateDataSetReference]: ...

@pulumi.output_type
class DashboardSourceEntitySourceTemplateDataSetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_set_arn: _builtins.str, data_set_placeholder: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetColumnGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        geo_spatial_column_group: Optional[
            outputs.DataSetColumnGroupGeoSpatialColumnGroup
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoSpatialColumnGroup")
    def geo_spatial_column_group(
        self,
    ) -> Optional[outputs.DataSetColumnGroupGeoSpatialColumnGroup]: ...

@pulumi.output_type
class DataSetColumnGroupGeoSpatialColumnGroup(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        columns: Sequence[_builtins.str],
        country_code: _builtins.str,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetColumnLevelPermissionRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_names: Optional[Sequence[_builtins.str]] = ...,
        principals: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataSetDataSetUsageConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_use_as_direct_query_source: Optional[_builtins.bool] = ...,
        disable_use_as_imported_source: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsDirectQuerySource")
    def disable_use_as_direct_query_source(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsImportedSource")
    def disable_use_as_imported_source(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataSetFieldFolder(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field_folders_id: _builtins.str,
        columns: Optional[Sequence[_builtins.str]] = ...,
        description: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fieldFoldersId")
    def field_folders_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        alias: _builtins.str,
        logical_table_map_id: _builtins.str,
        source: outputs.DataSetLogicalTableMapSource,
        data_transforms: Optional[
            Sequence[outputs.DataSetLogicalTableMapDataTransform]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="logicalTableMapId")
    def logical_table_map_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> outputs.DataSetLogicalTableMapSource: ...
    @_builtins.property
    @pulumi.getter(name="dataTransforms")
    def data_transforms(
        self,
    ) -> Optional[Sequence[outputs.DataSetLogicalTableMapDataTransform]]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransform(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cast_column_type_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformCastColumnTypeOperation
        ] = ...,
        create_columns_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformCreateColumnsOperation
        ] = ...,
        filter_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformFilterOperation
        ] = ...,
        project_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformProjectOperation
        ] = ...,
        rename_column_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformRenameColumnOperation
        ] = ...,
        tag_column_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformTagColumnOperation
        ] = ...,
        untag_column_operation: Optional[
            outputs.DataSetLogicalTableMapDataTransformUntagColumnOperation
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="castColumnTypeOperation")
    def cast_column_type_operation(
        self,
    ) -> Optional[
        outputs.DataSetLogicalTableMapDataTransformCastColumnTypeOperation
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createColumnsOperation")
    def create_columns_operation(
        self,
    ) -> Optional[
        outputs.DataSetLogicalTableMapDataTransformCreateColumnsOperation
    ]: ...
    @_builtins.property
    @pulumi.getter(name="filterOperation")
    def filter_operation(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapDataTransformFilterOperation]: ...
    @_builtins.property
    @pulumi.getter(name="projectOperation")
    def project_operation(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapDataTransformProjectOperation]: ...
    @_builtins.property
    @pulumi.getter(name="renameColumnOperation")
    def rename_column_operation(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapDataTransformRenameColumnOperation]: ...
    @_builtins.property
    @pulumi.getter(name="tagColumnOperation")
    def tag_column_operation(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapDataTransformTagColumnOperation]: ...
    @_builtins.property
    @pulumi.getter(name="untagColumnOperation")
    def untag_column_operation(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapDataTransformUntagColumnOperation]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformCastColumnTypeOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        new_column_type: _builtins.str,
        format: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newColumnType")
    def new_column_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformCreateColumnsOperation(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[
            outputs.DataSetLogicalTableMapDataTransformCreateColumnsOperationColumn
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Sequence[
        outputs.DataSetLogicalTableMapDataTransformCreateColumnsOperationColumn
    ]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformCreateColumnsOperationColumn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_id: _builtins.str,
        column_name: _builtins.str,
        expression: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnId")
    def column_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformFilterOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, condition_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformProjectOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, projected_columns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectedColumns")
    def projected_columns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformRenameColumnOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, column_name: _builtins.str, new_column_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newColumnName")
    def new_column_name(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformTagColumnOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        tags: Sequence[
            outputs.DataSetLogicalTableMapDataTransformTagColumnOperationTag
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Sequence[outputs.DataSetLogicalTableMapDataTransformTagColumnOperationTag]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformTagColumnOperationTag(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_description: Optional[
            outputs.DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescription
        ] = ...,
        column_geographic_role: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnDescription")
    def column_description(
        self,
    ) -> Optional[
        outputs.DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescription
    ]: ...
    @_builtins.property
    @pulumi.getter(name="columnGeographicRole")
    def column_geographic_role(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescription(dict):
    def __init__(__self__, *, text: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapDataTransformUntagColumnOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, column_name: _builtins.str, tag_names: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagNames")
    def tag_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapSource(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_set_arn: Optional[_builtins.str] = ...,
        join_instruction: Optional[
            outputs.DataSetLogicalTableMapSourceJoinInstruction
        ] = ...,
        physical_table_id: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="joinInstruction")
    def join_instruction(
        self,
    ) -> Optional[outputs.DataSetLogicalTableMapSourceJoinInstruction]: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableId")
    def physical_table_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetLogicalTableMapSourceJoinInstruction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        left_operand: _builtins.str,
        on_clause: _builtins.str,
        right_operand: _builtins.str,
        type: _builtins.str,
        left_join_key_properties: Optional[
            outputs.DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyProperties
        ] = ...,
        right_join_key_properties: Optional[
            outputs.DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyProperties
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leftOperand")
    def left_operand(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onClause")
    def on_clause(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rightOperand")
    def right_operand(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="leftJoinKeyProperties")
    def left_join_key_properties(
        self,
    ) -> Optional[
        outputs.DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyProperties
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rightJoinKeyProperties")
    def right_join_key_properties(
        self,
    ) -> Optional[
        outputs.DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyProperties
    ]: ...

@pulumi.output_type
class DataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, unique_key: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataSetLogicalTableMapSourceJoinInstructionRightJoinKeyProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, unique_key: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataSetOutputColumn(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetPermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetPhysicalTableMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        physical_table_map_id: _builtins.str,
        custom_sql: Optional[outputs.DataSetPhysicalTableMapCustomSql] = ...,
        relational_table: Optional[
            outputs.DataSetPhysicalTableMapRelationalTable
        ] = ...,
        s3_source: Optional[outputs.DataSetPhysicalTableMapS3Source] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableMapId")
    def physical_table_map_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="customSql")
    def custom_sql(self) -> Optional[outputs.DataSetPhysicalTableMapCustomSql]: ...
    @_builtins.property
    @pulumi.getter(name="relationalTable")
    def relational_table(
        self,
    ) -> Optional[outputs.DataSetPhysicalTableMapRelationalTable]: ...
    @_builtins.property
    @pulumi.getter(name="s3Source")
    def s3_source(self) -> Optional[outputs.DataSetPhysicalTableMapS3Source]: ...

@pulumi.output_type
class DataSetPhysicalTableMapCustomSql(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source_arn: _builtins.str,
        name: _builtins.str,
        sql_query: _builtins.str,
        columns: Optional[
            Sequence[outputs.DataSetPhysicalTableMapCustomSqlColumn]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlQuery")
    def sql_query(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Optional[Sequence[outputs.DataSetPhysicalTableMapCustomSqlColumn]]: ...

@pulumi.output_type
class DataSetPhysicalTableMapCustomSqlColumn(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetPhysicalTableMapRelationalTable(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source_arn: _builtins.str,
        input_columns: Sequence[
            outputs.DataSetPhysicalTableMapRelationalTableInputColumn
        ],
        name: _builtins.str,
        catalog: Optional[_builtins.str] = ...,
        schema: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> Sequence[outputs.DataSetPhysicalTableMapRelationalTableInputColumn]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetPhysicalTableMapRelationalTableInputColumn(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetPhysicalTableMapS3Source(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_source_arn: _builtins.str,
        input_columns: Sequence[outputs.DataSetPhysicalTableMapS3SourceInputColumn],
        upload_settings: outputs.DataSetPhysicalTableMapS3SourceUploadSettings,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> Sequence[outputs.DataSetPhysicalTableMapS3SourceInputColumn]: ...
    @_builtins.property
    @pulumi.getter(name="uploadSettings")
    def upload_settings(
        self,
    ) -> outputs.DataSetPhysicalTableMapS3SourceUploadSettings: ...

@pulumi.output_type
class DataSetPhysicalTableMapS3SourceInputColumn(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetPhysicalTableMapS3SourceUploadSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        contains_header: Optional[_builtins.bool] = ...,
        delimiter: Optional[_builtins.str] = ...,
        format: Optional[_builtins.str] = ...,
        start_from_row: Optional[_builtins.int] = ...,
        text_qualifier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containsHeader")
    def contains_header(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startFromRow")
    def start_from_row(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="textQualifier")
    def text_qualifier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetRefreshProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        refresh_configuration: outputs.DataSetRefreshPropertiesRefreshConfiguration,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="refreshConfiguration")
    def refresh_configuration(
        self,
    ) -> outputs.DataSetRefreshPropertiesRefreshConfiguration: ...

@pulumi.output_type
class DataSetRefreshPropertiesRefreshConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        incremental_refresh: outputs.DataSetRefreshPropertiesRefreshConfigurationIncrementalRefresh,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="incrementalRefresh")
    def incremental_refresh(
        self,
    ) -> outputs.DataSetRefreshPropertiesRefreshConfigurationIncrementalRefresh: ...

@pulumi.output_type
class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefresh(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        lookback_window: outputs.DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindow,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lookbackWindow")
    def lookback_window(
        self,
    ) -> outputs.DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindow: ...

@pulumi.output_type
class DataSetRefreshPropertiesRefreshConfigurationIncrementalRefreshLookbackWindow(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        size: _builtins.int,
        size_unit: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def size(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sizeUnit")
    def size_unit(self) -> _builtins.str: ...

@pulumi.output_type
class DataSetRowLevelPermissionDataSet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        permission_policy: _builtins.str,
        format_version: Optional[_builtins.str] = ...,
        namespace: Optional[_builtins.str] = ...,
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="permissionPolicy")
    def permission_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="formatVersion")
    def format_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetRowLevelPermissionTagConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tag_rules: Sequence[outputs.DataSetRowLevelPermissionTagConfigurationTagRule],
        status: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(
        self,
    ) -> Sequence[outputs.DataSetRowLevelPermissionTagConfigurationTagRule]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSetRowLevelPermissionTagConfigurationTagRule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        tag_key: _builtins.str,
        match_all_value: Optional[_builtins.str] = ...,
        tag_multi_value_delimiter: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchAllValue")
    def match_all_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="tagMultiValueDelimiter")
    def tag_multi_value_delimiter(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCredentials(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        copy_source_arn: Optional[_builtins.str] = ...,
        credential_pair: Optional[outputs.DataSourceCredentialsCredentialPair] = ...,
        secret_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="copySourceArn")
    def copy_source_arn(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="credentialPair")
    def credential_pair(
        self,
    ) -> Optional[outputs.DataSourceCredentialsCredentialPair]: ...
    @_builtins.property
    @pulumi.getter(name="secretArn")
    def secret_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceCredentialsCredentialPair(dict):
    def __init__(
        __self__, *, password: _builtins.str, username: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParameters(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        amazon_elasticsearch: Optional[
            outputs.DataSourceParametersAmazonElasticsearch
        ] = ...,
        athena: Optional[outputs.DataSourceParametersAthena] = ...,
        aurora: Optional[outputs.DataSourceParametersAurora] = ...,
        aurora_postgresql: Optional[outputs.DataSourceParametersAuroraPostgresql] = ...,
        aws_iot_analytics: Optional[outputs.DataSourceParametersAwsIotAnalytics] = ...,
        databricks: Optional[outputs.DataSourceParametersDatabricks] = ...,
        jira: Optional[outputs.DataSourceParametersJira] = ...,
        maria_db: Optional[outputs.DataSourceParametersMariaDb] = ...,
        mysql: Optional[outputs.DataSourceParametersMysql] = ...,
        oracle: Optional[outputs.DataSourceParametersOracle] = ...,
        postgresql: Optional[outputs.DataSourceParametersPostgresql] = ...,
        presto: Optional[outputs.DataSourceParametersPresto] = ...,
        rds: Optional[outputs.DataSourceParametersRds] = ...,
        redshift: Optional[outputs.DataSourceParametersRedshift] = ...,
        s3: Optional[outputs.DataSourceParametersS3] = ...,
        service_now: Optional[outputs.DataSourceParametersServiceNow] = ...,
        snowflake: Optional[outputs.DataSourceParametersSnowflake] = ...,
        spark: Optional[outputs.DataSourceParametersSpark] = ...,
        sql_server: Optional[outputs.DataSourceParametersSqlServer] = ...,
        teradata: Optional[outputs.DataSourceParametersTeradata] = ...,
        twitter: Optional[outputs.DataSourceParametersTwitter] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="amazonElasticsearch")
    def amazon_elasticsearch(
        self,
    ) -> Optional[outputs.DataSourceParametersAmazonElasticsearch]: ...
    @_builtins.property
    @pulumi.getter
    def athena(self) -> Optional[outputs.DataSourceParametersAthena]: ...
    @_builtins.property
    @pulumi.getter
    def aurora(self) -> Optional[outputs.DataSourceParametersAurora]: ...
    @_builtins.property
    @pulumi.getter(name="auroraPostgresql")
    def aurora_postgresql(
        self,
    ) -> Optional[outputs.DataSourceParametersAuroraPostgresql]: ...
    @_builtins.property
    @pulumi.getter(name="awsIotAnalytics")
    def aws_iot_analytics(
        self,
    ) -> Optional[outputs.DataSourceParametersAwsIotAnalytics]: ...
    @_builtins.property
    @pulumi.getter
    def databricks(self) -> Optional[outputs.DataSourceParametersDatabricks]: ...
    @_builtins.property
    @pulumi.getter
    def jira(self) -> Optional[outputs.DataSourceParametersJira]: ...
    @_builtins.property
    @pulumi.getter(name="mariaDb")
    def maria_db(self) -> Optional[outputs.DataSourceParametersMariaDb]: ...
    @_builtins.property
    @pulumi.getter
    def mysql(self) -> Optional[outputs.DataSourceParametersMysql]: ...
    @_builtins.property
    @pulumi.getter
    def oracle(self) -> Optional[outputs.DataSourceParametersOracle]: ...
    @_builtins.property
    @pulumi.getter
    def postgresql(self) -> Optional[outputs.DataSourceParametersPostgresql]: ...
    @_builtins.property
    @pulumi.getter
    def presto(self) -> Optional[outputs.DataSourceParametersPresto]: ...
    @_builtins.property
    @pulumi.getter
    def rds(self) -> Optional[outputs.DataSourceParametersRds]: ...
    @_builtins.property
    @pulumi.getter
    def redshift(self) -> Optional[outputs.DataSourceParametersRedshift]: ...
    @_builtins.property
    @pulumi.getter
    def s3(self) -> Optional[outputs.DataSourceParametersS3]: ...
    @_builtins.property
    @pulumi.getter(name="serviceNow")
    def service_now(self) -> Optional[outputs.DataSourceParametersServiceNow]: ...
    @_builtins.property
    @pulumi.getter
    def snowflake(self) -> Optional[outputs.DataSourceParametersSnowflake]: ...
    @_builtins.property
    @pulumi.getter
    def spark(self) -> Optional[outputs.DataSourceParametersSpark]: ...
    @_builtins.property
    @pulumi.getter(name="sqlServer")
    def sql_server(self) -> Optional[outputs.DataSourceParametersSqlServer]: ...
    @_builtins.property
    @pulumi.getter
    def teradata(self) -> Optional[outputs.DataSourceParametersTeradata]: ...
    @_builtins.property
    @pulumi.getter
    def twitter(self) -> Optional[outputs.DataSourceParametersTwitter]: ...

@pulumi.output_type
class DataSourceParametersAmazonElasticsearch(dict):
    def __init__(__self__, *, domain: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def domain(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersAthena(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, work_group: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workGroup")
    def work_group(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceParametersAurora(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersAuroraPostgresql(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersAwsIotAnalytics(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, data_set_name: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetName")
    def data_set_name(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersDatabricks(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        host: _builtins.str,
        port: _builtins.int,
        sql_endpoint_path: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="sqlEndpointPath")
    def sql_endpoint_path(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersJira(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, site_base_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteBaseUrl")
    def site_base_url(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersMariaDb(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersMysql(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersOracle(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersPostgresql(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersPresto(dict):
    def __init__(
        __self__, *, catalog: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersRds(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, database: _builtins.str, instance_id: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersRedshift(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        cluster_id: Optional[_builtins.str] = ...,
        host: Optional[_builtins.str] = ...,
        port: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class DataSourceParametersS3(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        manifest_file_location: outputs.DataSourceParametersS3ManifestFileLocation,
        role_arn: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manifestFileLocation")
    def manifest_file_location(
        self,
    ) -> outputs.DataSourceParametersS3ManifestFileLocation: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataSourceParametersS3ManifestFileLocation(dict):
    def __init__(__self__, *, bucket: _builtins.str, key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersServiceNow(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, site_base_url: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteBaseUrl")
    def site_base_url(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersSnowflake(dict):
    def __init__(
        __self__,
        *,
        database: _builtins.str,
        host: _builtins.str,
        warehouse: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def warehouse(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceParametersSpark(dict):
    def __init__(__self__, *, host: _builtins.str, port: _builtins.int) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersSqlServer(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersTeradata(dict):
    def __init__(
        __self__, *, database: _builtins.str, host: _builtins.str, port: _builtins.int
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def database(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> _builtins.int: ...

@pulumi.output_type
class DataSourceParametersTwitter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, max_rows: _builtins.int, query: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxRows")
    def max_rows(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourcePermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class DataSourceSslProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, disable_ssl: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableSsl")
    def disable_ssl(self) -> _builtins.bool: ...

@pulumi.output_type
class DataSourceVpcConnectionProperties(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, vpc_connection_arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="vpcConnectionArn")
    def vpc_connection_arn(self) -> _builtins.str: ...

@pulumi.output_type
class FolderPermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class IamPolicyAssignmentIdentities(dict):
    def __init__(
        __self__,
        *,
        groups: Optional[Sequence[_builtins.str]] = ...,
        users: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def users(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class KeyRegistrationKeyRegistration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key_arn: _builtins.str, default_key: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyArn")
    def key_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="defaultKey")
    def default_key(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class NamespaceTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RefreshScheduleSchedule(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        refresh_type: _builtins.str,
        schedule_frequency: outputs.RefreshScheduleScheduleScheduleFrequency,
        start_after_date_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="refreshType")
    def refresh_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="scheduleFrequency")
    def schedule_frequency(
        self,
    ) -> outputs.RefreshScheduleScheduleScheduleFrequency: ...
    @_builtins.property
    @pulumi.getter(name="startAfterDateTime")
    def start_after_date_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RefreshScheduleScheduleScheduleFrequency(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        interval: _builtins.str,
        refresh_on_day: Optional[
            outputs.RefreshScheduleScheduleScheduleFrequencyRefreshOnDay
        ] = ...,
        time_of_the_day: Optional[_builtins.str] = ...,
        timezone: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def interval(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="refreshOnDay")
    def refresh_on_day(
        self,
    ) -> Optional[outputs.RefreshScheduleScheduleScheduleFrequencyRefreshOnDay]: ...
    @_builtins.property
    @pulumi.getter(name="timeOfTheDay")
    def time_of_the_day(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timezone(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RefreshScheduleScheduleScheduleFrequencyRefreshOnDay(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        day_of_month: Optional[_builtins.str] = ...,
        day_of_week: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dayOfMonth")
    def day_of_month(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TemplatePermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class TemplateSourceEntity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        source_analysis: Optional[outputs.TemplateSourceEntitySourceAnalysis] = ...,
        source_template: Optional[outputs.TemplateSourceEntitySourceTemplate] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sourceAnalysis")
    def source_analysis(
        self,
    ) -> Optional[outputs.TemplateSourceEntitySourceAnalysis]: ...
    @_builtins.property
    @pulumi.getter(name="sourceTemplate")
    def source_template(
        self,
    ) -> Optional[outputs.TemplateSourceEntitySourceTemplate]: ...

@pulumi.output_type
class TemplateSourceEntitySourceAnalysis(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        data_set_references: Sequence[
            outputs.TemplateSourceEntitySourceAnalysisDataSetReference
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetReferences")
    def data_set_references(
        self,
    ) -> Sequence[outputs.TemplateSourceEntitySourceAnalysisDataSetReference]: ...

@pulumi.output_type
class TemplateSourceEntitySourceAnalysisDataSetReference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_set_arn: _builtins.str, data_set_placeholder: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSetPlaceholder")
    def data_set_placeholder(self) -> _builtins.str: ...

@pulumi.output_type
class TemplateSourceEntitySourceTemplate(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class ThemeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_color_palette: Optional[outputs.ThemeConfigurationDataColorPalette] = ...,
        sheet: Optional[outputs.ThemeConfigurationSheet] = ...,
        typography: Optional[outputs.ThemeConfigurationTypography] = ...,
        ui_color_palette: Optional[outputs.ThemeConfigurationUiColorPalette] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataColorPalette")
    def data_color_palette(
        self,
    ) -> Optional[outputs.ThemeConfigurationDataColorPalette]: ...
    @_builtins.property
    @pulumi.getter
    def sheet(self) -> Optional[outputs.ThemeConfigurationSheet]: ...
    @_builtins.property
    @pulumi.getter
    def typography(self) -> Optional[outputs.ThemeConfigurationTypography]: ...
    @_builtins.property
    @pulumi.getter(name="uiColorPalette")
    def ui_color_palette(
        self,
    ) -> Optional[outputs.ThemeConfigurationUiColorPalette]: ...

@pulumi.output_type
class ThemeConfigurationDataColorPalette(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        colors: Optional[Sequence[_builtins.str]] = ...,
        empty_fill_color: Optional[_builtins.str] = ...,
        min_max_gradients: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def colors(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="emptyFillColor")
    def empty_fill_color(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="minMaxGradients")
    def min_max_gradients(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ThemeConfigurationSheet(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        tile: Optional[outputs.ThemeConfigurationSheetTile] = ...,
        tile_layout: Optional[outputs.ThemeConfigurationSheetTileLayout] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def tile(self) -> Optional[outputs.ThemeConfigurationSheetTile]: ...
    @_builtins.property
    @pulumi.getter(name="tileLayout")
    def tile_layout(self) -> Optional[outputs.ThemeConfigurationSheetTileLayout]: ...

@pulumi.output_type
class ThemeConfigurationSheetTile(dict):
    def __init__(
        __self__, *, border: Optional[outputs.ThemeConfigurationSheetTileBorder] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def border(self) -> Optional[outputs.ThemeConfigurationSheetTileBorder]: ...

@pulumi.output_type
class ThemeConfigurationSheetTileBorder(dict):
    def __init__(__self__, *, show: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ThemeConfigurationSheetTileLayout(dict):
    def __init__(
        __self__,
        *,
        gutter: Optional[outputs.ThemeConfigurationSheetTileLayoutGutter] = ...,
        margin: Optional[outputs.ThemeConfigurationSheetTileLayoutMargin] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gutter(self) -> Optional[outputs.ThemeConfigurationSheetTileLayoutGutter]: ...
    @_builtins.property
    @pulumi.getter
    def margin(self) -> Optional[outputs.ThemeConfigurationSheetTileLayoutMargin]: ...

@pulumi.output_type
class ThemeConfigurationSheetTileLayoutGutter(dict):
    def __init__(__self__, *, show: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ThemeConfigurationSheetTileLayoutMargin(dict):
    def __init__(__self__, *, show: Optional[_builtins.bool] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ThemeConfigurationTypography(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        font_families: Optional[
            Sequence[outputs.ThemeConfigurationTypographyFontFamily]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamilies")
    def font_families(
        self,
    ) -> Optional[Sequence[outputs.ThemeConfigurationTypographyFontFamily]]: ...

@pulumi.output_type
class ThemeConfigurationTypographyFontFamily(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, font_family: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamily")
    def font_family(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ThemeConfigurationUiColorPalette(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        accent: Optional[_builtins.str] = ...,
        accent_foreground: Optional[_builtins.str] = ...,
        danger: Optional[_builtins.str] = ...,
        danger_foreground: Optional[_builtins.str] = ...,
        dimension: Optional[_builtins.str] = ...,
        dimension_foreground: Optional[_builtins.str] = ...,
        measure: Optional[_builtins.str] = ...,
        measure_foreground: Optional[_builtins.str] = ...,
        primary_background: Optional[_builtins.str] = ...,
        primary_foreground: Optional[_builtins.str] = ...,
        secondary_background: Optional[_builtins.str] = ...,
        secondary_foreground: Optional[_builtins.str] = ...,
        success: Optional[_builtins.str] = ...,
        success_foreground: Optional[_builtins.str] = ...,
        warning: Optional[_builtins.str] = ...,
        warning_foreground: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="accentForeground")
    def accent_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def danger(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dangerForeground")
    def danger_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dimensionForeground")
    def dimension_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def measure(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="measureForeground")
    def measure_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryBackground")
    def primary_background(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="primaryForeground")
    def primary_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBackground")
    def secondary_background(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secondaryForeground")
    def secondary_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def success(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="successForeground")
    def success_foreground(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def warning(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="warningForeground")
    def warning_foreground(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ThemePermission(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class VpcConnectionTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GetDataSetColumnGroupResult(dict):
    def __init__(
        __self__,
        *,
        geo_spatial_column_groups: Sequence[
            outputs.GetDataSetColumnGroupGeoSpatialColumnGroupResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="geoSpatialColumnGroups")
    def geo_spatial_column_groups(
        self,
    ) -> Sequence[outputs.GetDataSetColumnGroupGeoSpatialColumnGroupResult]: ...

@pulumi.output_type
class GetDataSetColumnGroupGeoSpatialColumnGroupResult(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[_builtins.str],
        country_code: _builtins.str,
        name: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetColumnLevelPermissionRuleResult(dict):
    def __init__(
        __self__,
        *,
        column_names: Sequence[_builtins.str],
        principals: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnNames")
    def column_names(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principals(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDataSetDataSetUsageConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        disable_use_as_direct_query_source: _builtins.bool,
        disable_use_as_imported_source: _builtins.bool,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsDirectQuerySource")
    def disable_use_as_direct_query_source(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="disableUseAsImportedSource")
    def disable_use_as_imported_source(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataSetFieldFolderResult(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[_builtins.str],
        description: _builtins.str,
        field_folders_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fieldFoldersId")
    def field_folders_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapResult(dict):
    def __init__(
        __self__,
        *,
        alias: _builtins.str,
        data_transforms: Sequence[outputs.GetDataSetLogicalTableMapDataTransformResult],
        logical_table_map_id: _builtins.str,
        sources: Sequence[outputs.GetDataSetLogicalTableMapSourceResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def alias(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataTransforms")
    def data_transforms(
        self,
    ) -> Sequence[outputs.GetDataSetLogicalTableMapDataTransformResult]: ...
    @_builtins.property
    @pulumi.getter(name="logicalTableMapId")
    def logical_table_map_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sources(self) -> Sequence[outputs.GetDataSetLogicalTableMapSourceResult]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformResult(dict):
    def __init__(
        __self__,
        *,
        cast_column_type_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformCastColumnTypeOperationResult
        ],
        create_columns_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformCreateColumnsOperationResult
        ],
        filter_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformFilterOperationResult
        ],
        project_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformProjectOperationResult
        ],
        rename_column_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformRenameColumnOperationResult
        ],
        tag_column_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationResult
        ],
        untag_column_operations: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformUntagColumnOperationResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="castColumnTypeOperations")
    def cast_column_type_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformCastColumnTypeOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="createColumnsOperations")
    def create_columns_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformCreateColumnsOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="filterOperations")
    def filter_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformFilterOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="projectOperations")
    def project_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformProjectOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="renameColumnOperations")
    def rename_column_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformRenameColumnOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="tagColumnOperations")
    def tag_column_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="untagColumnOperations")
    def untag_column_operations(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformUntagColumnOperationResult
    ]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformCastColumnTypeOperationResult(dict):
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        format: _builtins.str,
        new_column_type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newColumnType")
    def new_column_type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformCreateColumnsOperationResult(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformCreateColumnsOperationColumnResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformCreateColumnsOperationColumnResult
    ]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformCreateColumnsOperationColumnResult(dict):
    def __init__(
        __self__,
        *,
        column_id: _builtins.str,
        column_name: _builtins.str,
        expression: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnId")
    def column_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformFilterOperationResult(dict):
    def __init__(__self__, *, condition_expression: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionExpression")
    def condition_expression(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformProjectOperationResult(dict):
    def __init__(__self__, *, projected_columns: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="projectedColumns")
    def projected_columns(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformRenameColumnOperationResult(dict):
    def __init__(
        __self__, *, column_name: _builtins.str, new_column_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="newColumnName")
    def new_column_name(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformTagColumnOperationResult(dict):
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        tags: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationTagResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationTagResult
    ]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformTagColumnOperationTagResult(dict):
    def __init__(
        __self__,
        *,
        column_descriptions: Sequence[
            outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionResult
        ],
        column_geographic_role: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnDescriptions")
    def column_descriptions(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="columnGeographicRole")
    def column_geographic_role(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformTagColumnOperationTagColumnDescriptionResult(
    dict
):
    def __init__(__self__, *, text: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapDataTransformUntagColumnOperationResult(dict):
    def __init__(
        __self__, *, column_name: _builtins.str, tag_names: Sequence[_builtins.str]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagNames")
    def tag_names(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetDataSetLogicalTableMapSourceResult(dict):
    def __init__(
        __self__,
        *,
        data_set_arn: _builtins.str,
        join_instructions: Sequence[
            outputs.GetDataSetLogicalTableMapSourceJoinInstructionResult
        ],
        physical_table_id: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSetArn")
    def data_set_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="joinInstructions")
    def join_instructions(
        self,
    ) -> Sequence[outputs.GetDataSetLogicalTableMapSourceJoinInstructionResult]: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableId")
    def physical_table_id(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapSourceJoinInstructionResult(dict):
    def __init__(
        __self__,
        *,
        left_join_key_properties: Sequence[
            outputs.GetDataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertyResult
        ],
        left_operand: _builtins.str,
        on_clause: _builtins.str,
        right_join_key_properties: Sequence[
            outputs.GetDataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertyResult
        ],
        right_operand: _builtins.str,
        type: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="leftJoinKeyProperties")
    def left_join_key_properties(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="leftOperand")
    def left_operand(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="onClause")
    def on_clause(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="rightJoinKeyProperties")
    def right_join_key_properties(
        self,
    ) -> Sequence[
        outputs.GetDataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertyResult
    ]: ...
    @_builtins.property
    @pulumi.getter(name="rightOperand")
    def right_operand(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetLogicalTableMapSourceJoinInstructionLeftJoinKeyPropertyResult(dict):
    def __init__(__self__, *, unique_key: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataSetLogicalTableMapSourceJoinInstructionRightJoinKeyPropertyResult(dict):
    def __init__(__self__, *, unique_key: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="uniqueKey")
    def unique_key(self) -> _builtins.bool: ...

@pulumi.output_type
class GetDataSetPermissionResult(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapResult(dict):
    def __init__(
        __self__,
        *,
        custom_sqls: Sequence[outputs.GetDataSetPhysicalTableMapCustomSqlResult],
        physical_table_map_id: _builtins.str,
        relational_tables: Sequence[
            outputs.GetDataSetPhysicalTableMapRelationalTableResult
        ],
        s3_sources: Sequence[outputs.GetDataSetPhysicalTableMapS3SourceResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customSqls")
    def custom_sqls(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapCustomSqlResult]: ...
    @_builtins.property
    @pulumi.getter(name="physicalTableMapId")
    def physical_table_map_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="relationalTables")
    def relational_tables(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapRelationalTableResult]: ...
    @_builtins.property
    @pulumi.getter(name="s3Sources")
    def s3_sources(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapS3SourceResult]: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapCustomSqlResult(dict):
    def __init__(
        __self__,
        *,
        columns: Sequence[outputs.GetDataSetPhysicalTableMapCustomSqlColumnResult],
        data_source_arn: _builtins.str,
        name: _builtins.str,
        sql_query: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def columns(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapCustomSqlColumnResult]: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sqlQuery")
    def sql_query(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapCustomSqlColumnResult(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapRelationalTableResult(dict):
    def __init__(
        __self__,
        *,
        catalog: _builtins.str,
        data_source_arn: _builtins.str,
        input_columns: Sequence[
            outputs.GetDataSetPhysicalTableMapRelationalTableInputColumnResult
        ],
        name: _builtins.str,
        schema: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def catalog(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> Sequence[
        outputs.GetDataSetPhysicalTableMapRelationalTableInputColumnResult
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapRelationalTableInputColumnResult(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapS3SourceResult(dict):
    def __init__(
        __self__,
        *,
        data_source_arn: _builtins.str,
        input_columns: Sequence[
            outputs.GetDataSetPhysicalTableMapS3SourceInputColumnResult
        ],
        upload_settings: Sequence[
            outputs.GetDataSetPhysicalTableMapS3SourceUploadSettingResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataSourceArn")
    def data_source_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="inputColumns")
    def input_columns(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapS3SourceInputColumnResult]: ...
    @_builtins.property
    @pulumi.getter(name="uploadSettings")
    def upload_settings(
        self,
    ) -> Sequence[outputs.GetDataSetPhysicalTableMapS3SourceUploadSettingResult]: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapS3SourceInputColumnResult(dict):
    def __init__(__self__, *, name: _builtins.str, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetPhysicalTableMapS3SourceUploadSettingResult(dict):
    def __init__(
        __self__,
        *,
        contains_header: _builtins.bool,
        delimiter: _builtins.str,
        format: _builtins.str,
        start_from_row: _builtins.int,
        text_qualifier: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containsHeader")
    def contains_header(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter
    def delimiter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startFromRow")
    def start_from_row(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="textQualifier")
    def text_qualifier(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetRowLevelPermissionDataSetResult(dict):
    def __init__(
        __self__,
        *,
        arn: _builtins.str,
        format_version: _builtins.str,
        namespace: _builtins.str,
        permission_policy: _builtins.str,
        status: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="formatVersion")
    def format_version(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def namespace(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="permissionPolicy")
    def permission_policy(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...

@pulumi.output_type
class GetDataSetRowLevelPermissionTagConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        status: _builtins.str,
        tag_rules: Sequence[
            outputs.GetDataSetRowLevelPermissionTagConfigurationTagRuleResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagRules")
    def tag_rules(
        self,
    ) -> Sequence[
        outputs.GetDataSetRowLevelPermissionTagConfigurationTagRuleResult
    ]: ...

@pulumi.output_type
class GetDataSetRowLevelPermissionTagConfigurationTagRuleResult(dict):
    def __init__(
        __self__,
        *,
        column_name: _builtins.str,
        match_all_value: _builtins.str,
        tag_key: _builtins.str,
        tag_multi_value_delimiter: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="columnName")
    def column_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="matchAllValue")
    def match_all_value(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagKey")
    def tag_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tagMultiValueDelimiter")
    def tag_multi_value_delimiter(self) -> _builtins.str: ...

@pulumi.output_type
class GetQuicksightAnalysisPermissionResult(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...

@pulumi.output_type
class GetThemeConfigurationResult(dict):
    def __init__(
        __self__,
        *,
        data_color_palettes: Sequence[
            outputs.GetThemeConfigurationDataColorPaletteResult
        ],
        sheets: Sequence[outputs.GetThemeConfigurationSheetResult],
        typographies: Sequence[outputs.GetThemeConfigurationTypographyResult],
        ui_color_palettes: Sequence[outputs.GetThemeConfigurationUiColorPaletteResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataColorPalettes")
    def data_color_palettes(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationDataColorPaletteResult]: ...
    @_builtins.property
    @pulumi.getter
    def sheets(self) -> Sequence[outputs.GetThemeConfigurationSheetResult]: ...
    @_builtins.property
    @pulumi.getter
    def typographies(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationTypographyResult]: ...
    @_builtins.property
    @pulumi.getter(name="uiColorPalettes")
    def ui_color_palettes(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationUiColorPaletteResult]: ...

@pulumi.output_type
class GetThemeConfigurationDataColorPaletteResult(dict):
    def __init__(
        __self__,
        *,
        colors: Sequence[_builtins.str],
        empty_fill_color: _builtins.str,
        min_max_gradients: Sequence[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def colors(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="emptyFillColor")
    def empty_fill_color(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="minMaxGradients")
    def min_max_gradients(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class GetThemeConfigurationSheetResult(dict):
    def __init__(
        __self__,
        *,
        tile_layouts: Sequence[outputs.GetThemeConfigurationSheetTileLayoutResult],
        tiles: Sequence[outputs.GetThemeConfigurationSheetTileResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="tileLayouts")
    def tile_layouts(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationSheetTileLayoutResult]: ...
    @_builtins.property
    @pulumi.getter
    def tiles(self) -> Sequence[outputs.GetThemeConfigurationSheetTileResult]: ...

@pulumi.output_type
class GetThemeConfigurationSheetTileResult(dict):
    def __init__(
        __self__,
        *,
        borders: Sequence[outputs.GetThemeConfigurationSheetTileBorderResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def borders(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationSheetTileBorderResult]: ...

@pulumi.output_type
class GetThemeConfigurationSheetTileBorderResult(dict):
    def __init__(__self__, *, show: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> _builtins.bool: ...

@pulumi.output_type
class GetThemeConfigurationSheetTileLayoutResult(dict):
    def __init__(
        __self__,
        *,
        gutters: Sequence[outputs.GetThemeConfigurationSheetTileLayoutGutterResult],
        margins: Sequence[outputs.GetThemeConfigurationSheetTileLayoutMarginResult],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def gutters(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationSheetTileLayoutGutterResult]: ...
    @_builtins.property
    @pulumi.getter
    def margins(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationSheetTileLayoutMarginResult]: ...

@pulumi.output_type
class GetThemeConfigurationSheetTileLayoutGutterResult(dict):
    def __init__(__self__, *, show: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> _builtins.bool: ...

@pulumi.output_type
class GetThemeConfigurationSheetTileLayoutMarginResult(dict):
    def __init__(__self__, *, show: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter
    def show(self) -> _builtins.bool: ...

@pulumi.output_type
class GetThemeConfigurationTypographyResult(dict):
    def __init__(
        __self__,
        *,
        font_families: Sequence[
            outputs.GetThemeConfigurationTypographyFontFamilyResult
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamilies")
    def font_families(
        self,
    ) -> Sequence[outputs.GetThemeConfigurationTypographyFontFamilyResult]: ...

@pulumi.output_type
class GetThemeConfigurationTypographyFontFamilyResult(dict):
    def __init__(__self__, *, font_family: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fontFamily")
    def font_family(self) -> _builtins.str: ...

@pulumi.output_type
class GetThemeConfigurationUiColorPaletteResult(dict):
    def __init__(
        __self__,
        *,
        accent: _builtins.str,
        accent_foreground: _builtins.str,
        danger: _builtins.str,
        danger_foreground: _builtins.str,
        dimension: _builtins.str,
        dimension_foreground: _builtins.str,
        measure: _builtins.str,
        measure_foreground: _builtins.str,
        primary_background: _builtins.str,
        primary_foreground: _builtins.str,
        secondary_background: _builtins.str,
        secondary_foreground: _builtins.str,
        success: _builtins.str,
        success_foreground: _builtins.str,
        warning: _builtins.str,
        warning_foreground: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="accentForeground")
    def accent_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def danger(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dangerForeground")
    def danger_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def dimension(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="dimensionForeground")
    def dimension_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def measure(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="measureForeground")
    def measure_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryBackground")
    def primary_background(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="primaryForeground")
    def primary_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryBackground")
    def secondary_background(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secondaryForeground")
    def secondary_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def success(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="successForeground")
    def success_foreground(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def warning(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="warningForeground")
    def warning_foreground(self) -> _builtins.str: ...

@pulumi.output_type
class GetThemePermissionResult(dict):
    def __init__(
        __self__, *, actions: Sequence[_builtins.str], principal: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def principal(self) -> _builtins.str: ...
