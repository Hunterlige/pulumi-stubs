import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, overload

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["ReportDefinitionArgs", "ReportDefinition"]

@pulumi.input_type
class ReportDefinitionArgs:
    def __init__(
        __self__,
        *,
        additional_schema_elements: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        compression: pulumi.Input[_builtins.str],
        format: pulumi.Input[_builtins.str],
        report_name: pulumi.Input[_builtins.str],
        s3_bucket: pulumi.Input[_builtins.str],
        s3_prefix: pulumi.Input[_builtins.str],
        s3_region: pulumi.Input[_builtins.str],
        time_unit: pulumi.Input[_builtins.str],
        additional_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        refresh_closed_reports: Optional[pulumi.Input[_builtins.bool]] = ...,
        report_versioning: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalSchemaElements")
    def additional_schema_elements(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @additional_schema_elements.setter
    def additional_schema_elements(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> pulumi.Input[_builtins.str]: ...
    @compression.setter
    def compression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Input[_builtins.str]: ...
    @format.setter
    def format(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[_builtins.str]: ...
    @report_name.setter
    def report_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Input[_builtins.str]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> pulumi.Input[_builtins.str]: ...
    @s3_prefix.setter
    def s3_prefix(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> pulumi.Input[_builtins.str]: ...
    @s3_region.setter
    def s3_region(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Input[_builtins.str]: ...
    @time_unit.setter
    def time_unit(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalArtifacts")
    def additional_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_artifacts.setter
    def additional_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="refreshClosedReports")
    def refresh_closed_reports(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @refresh_closed_reports.setter
    def refresh_closed_reports(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="reportVersioning")
    def report_versioning(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @report_versioning.setter
    def report_versioning(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

@pulumi.input_type
class _ReportDefinitionState:
    def __init__(
        __self__,
        *,
        additional_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_schema_elements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_closed_reports: Optional[pulumi.Input[_builtins.bool]] = ...,
        report_name: Optional[pulumi.Input[_builtins.str]] = ...,
        report_versioning: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalArtifacts")
    def additional_artifacts(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_artifacts.setter
    def additional_artifacts(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="additionalSchemaElements")
    def additional_schema_elements(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @additional_schema_elements.setter
    def additional_schema_elements(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @compression.setter
    def compression(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @format.setter
    def format(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="refreshClosedReports")
    def refresh_closed_reports(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @refresh_closed_reports.setter
    def refresh_closed_reports(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @report_name.setter
    def report_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="reportVersioning")
    def report_versioning(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @report_versioning.setter
    def report_versioning(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_bucket.setter
    def s3_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_prefix.setter
    def s3_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @s3_region.setter
    def s3_region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_unit.setter
    def time_unit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:cur/reportDefinition:ReportDefinition")
class ReportDefinition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_schema_elements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_closed_reports: Optional[pulumi.Input[_builtins.bool]] = ...,
        report_name: Optional[pulumi.Input[_builtins.str]] = ...,
        report_versioning: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: ReportDefinitionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        additional_artifacts: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        additional_schema_elements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        compression: Optional[pulumi.Input[_builtins.str]] = ...,
        format: Optional[pulumi.Input[_builtins.str]] = ...,
        refresh_closed_reports: Optional[pulumi.Input[_builtins.bool]] = ...,
        report_name: Optional[pulumi.Input[_builtins.str]] = ...,
        report_versioning: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
        s3_region: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        time_unit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> ReportDefinition: ...
    @_builtins.property
    @pulumi.getter(name="additionalArtifacts")
    def additional_artifacts(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="additionalSchemaElements")
    def additional_schema_elements(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def compression(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def format(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="refreshClosedReports")
    def refresh_closed_reports(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="reportVersioning")
    def report_versioning(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="s3Bucket")
    def s3_bucket(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Prefix")
    def s3_prefix(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="s3Region")
    def s3_region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeUnit")
    def time_unit(self) -> pulumi.Output[_builtins.str]: ...
