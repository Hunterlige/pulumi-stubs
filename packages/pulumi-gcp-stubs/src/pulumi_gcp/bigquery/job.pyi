import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["JobArgs", "Job"]

@pulumi.input_type
class JobArgs:
    def __init__(
        __self__,
        *,
        job_id: pulumi.Input[_builtins.str],
        copy: Optional[pulumi.Input[JobCopyArgs]] = ...,
        extract: Optional[pulumi.Input[JobExtractArgs]] = ...,
        job_timeout_ms: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load: Optional[pulumi.Input[JobLoadArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[JobQueryArgs]] = ...,
        reservation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Input[_builtins.str]: ...
    @job_id.setter
    def job_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def copy(self) -> Optional[pulumi.Input[JobCopyArgs]]: ...
    @copy.setter
    def copy(self, value: Optional[pulumi.Input[JobCopyArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def extract(self) -> Optional[pulumi.Input[JobExtractArgs]]: ...
    @extract.setter
    def extract(self, value: Optional[pulumi.Input[JobExtractArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="jobTimeoutMs")
    def job_timeout_ms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_timeout_ms.setter
    def job_timeout_ms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def load(self) -> Optional[pulumi.Input[JobLoadArgs]]: ...
    @load.setter
    def load(self, value: Optional[pulumi.Input[JobLoadArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[JobQueryArgs]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[JobQueryArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation.setter
    def reservation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _JobState:
    def __init__(
        __self__,
        *,
        copy: Optional[pulumi.Input[JobCopyArgs]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        extract: Optional[pulumi.Input[JobExtractArgs]] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_timeout_ms: Optional[pulumi.Input[_builtins.str]] = ...,
        job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load: Optional[pulumi.Input[JobLoadArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query: Optional[pulumi.Input[JobQueryArgs]] = ...,
        reservation: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]] = ...,
        user_email: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def copy(self) -> Optional[pulumi.Input[JobCopyArgs]]: ...
    @copy.setter
    def copy(self, value: Optional[pulumi.Input[JobCopyArgs]]): ...
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
    @pulumi.getter
    def extract(self) -> Optional[pulumi.Input[JobExtractArgs]]: ...
    @extract.setter
    def extract(self, value: Optional[pulumi.Input[JobExtractArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobTimeoutMs")
    def job_timeout_ms(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_timeout_ms.setter
    def job_timeout_ms(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    def load(self) -> Optional[pulumi.Input[JobLoadArgs]]: ...
    @load.setter
    def load(self, value: Optional[pulumi.Input[JobLoadArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[JobQueryArgs]]: ...
    @query.setter
    def query(self, value: Optional[pulumi.Input[JobQueryArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reservation.setter
    def reservation(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def statuses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]]: ...
    @statuses.setter
    def statuses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[JobStatusArgs]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @user_email.setter
    def user_email(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("gcp:bigquery/job:Job")
class Job(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        copy: Optional[pulumi.Input[Union[JobCopyArgs, JobCopyArgsDict]]] = ...,
        extract: Optional[
            pulumi.Input[Union[JobExtractArgs, JobExtractArgsDict]]
        ] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_timeout_ms: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load: Optional[pulumi.Input[Union[JobLoadArgs, JobLoadArgsDict]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        query: Optional[pulumi.Input[Union[JobQueryArgs, JobQueryArgsDict]]] = ...,
        reservation: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: JobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        copy: Optional[pulumi.Input[Union[JobCopyArgs, JobCopyArgsDict]]] = ...,
        effective_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        extract: Optional[
            pulumi.Input[Union[JobExtractArgs, JobExtractArgsDict]]
        ] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_timeout_ms: Optional[pulumi.Input[_builtins.str]] = ...,
        job_type: Optional[pulumi.Input[_builtins.str]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        load: Optional[pulumi.Input[Union[JobLoadArgs, JobLoadArgsDict]]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        pulumi_labels: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        query: Optional[pulumi.Input[Union[JobQueryArgs, JobQueryArgsDict]]] = ...,
        reservation: Optional[pulumi.Input[_builtins.str]] = ...,
        statuses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[Union[JobStatusArgs, JobStatusArgsDict]]]
            ]
        ] = ...,
        user_email: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> Job: ...
    @_builtins.property
    @pulumi.getter
    def copy(self) -> pulumi.Output[Optional[outputs.JobCopy]]: ...
    @_builtins.property
    @pulumi.getter(name="effectiveLabels")
    def effective_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def extract(self) -> pulumi.Output[Optional[outputs.JobExtract]]: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobTimeoutMs")
    def job_timeout_ms(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def load(self) -> pulumi.Output[Optional[outputs.JobLoad]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pulumiLabels")
    def pulumi_labels(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def query(self) -> pulumi.Output[Optional[outputs.JobQuery]]: ...
    @_builtins.property
    @pulumi.getter
    def reservation(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence[outputs.JobStatus]]: ...
    @_builtins.property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Output[_builtins.str]: ...
