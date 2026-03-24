import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["SigningJobArgs", "SigningJob"]

@pulumi.input_type
class SigningJobArgs:
    def __init__(
        __self__,
        *,
        destination: pulumi.Input[SigningJobDestinationArgs],
        profile_name: pulumi.Input[_builtins.str],
        source: pulumi.Input[SigningJobSourceArgs],
        ignore_signing_job_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Input[SigningJobDestinationArgs]: ...
    @destination.setter
    def destination(self, value: pulumi.Input[SigningJobDestinationArgs]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[_builtins.str]: ...
    @profile_name.setter
    def profile_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Input[SigningJobSourceArgs]: ...
    @source.setter
    def source(self, value: pulumi.Input[SigningJobSourceArgs]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreSigningJobFailure")
    def ignore_signing_job_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_signing_job_failure.setter
    def ignore_signing_job_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.input_type
class _SigningJobState:
    def __init__(
        __self__,
        *,
        completed_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[pulumi.Input[SigningJobDestinationArgs]] = ...,
        ignore_signing_job_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_invoker: Optional[pulumi.Input[_builtins.str]] = ...,
        job_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requested_by: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_records: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobRevocationRecordArgs]]]
        ] = ...,
        signature_expires_at: Optional[pulumi.Input[_builtins.str]] = ...,
        signed_objects: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectArgs]]]
        ] = ...,
        source: Optional[pulumi.Input[SigningJobSourceArgs]] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @completed_at.setter
    def completed_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[SigningJobDestinationArgs]]: ...
    @destination.setter
    def destination(self, value: Optional[pulumi.Input[SigningJobDestinationArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreSigningJobFailure")
    def ignore_signing_job_failure(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_signing_job_failure.setter
    def ignore_signing_job_failure(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_id.setter
    def job_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobInvoker")
    def job_invoker(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_invoker.setter
    def job_invoker(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="jobOwner")
    def job_owner(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @job_owner.setter
    def job_owner(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_display_name.setter
    def platform_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @platform_id.setter
    def platform_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_version.setter
    def profile_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestedBy")
    def requested_by(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @requested_by.setter
    def requested_by(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[SigningJobRevocationRecordArgs]]]
    ]: ...
    @revocation_records.setter
    def revocation_records(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobRevocationRecordArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="signatureExpiresAt")
    def signature_expires_at(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signature_expires_at.setter
    def signature_expires_at(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signedObjects")
    def signed_objects(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectArgs]]]]: ...
    @signed_objects.setter
    def signed_objects(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[SigningJobSignedObjectArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[SigningJobSourceArgs]]: ...
    @source.setter
    def source(self, value: Optional[pulumi.Input[SigningJobSourceArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @status_reason.setter
    def status_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token("aws:signer/signingJob:SigningJob")
class SigningJob(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        destination: Optional[
            pulumi.Input[
                Union[SigningJobDestinationArgs, SigningJobDestinationArgsDict]
            ]
        ] = ...,
        ignore_signing_job_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        source: Optional[
            pulumi.Input[Union[SigningJobSourceArgs, SigningJobSourceArgsDict]]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: SigningJobArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        completed_at: Optional[pulumi.Input[_builtins.str]] = ...,
        created_at: Optional[pulumi.Input[_builtins.str]] = ...,
        destination: Optional[
            pulumi.Input[
                Union[SigningJobDestinationArgs, SigningJobDestinationArgsDict]
            ]
        ] = ...,
        ignore_signing_job_failure: Optional[pulumi.Input[_builtins.bool]] = ...,
        job_id: Optional[pulumi.Input[_builtins.str]] = ...,
        job_invoker: Optional[pulumi.Input[_builtins.str]] = ...,
        job_owner: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        platform_id: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_name: Optional[pulumi.Input[_builtins.str]] = ...,
        profile_version: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requested_by: Optional[pulumi.Input[_builtins.str]] = ...,
        revocation_records: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SigningJobRevocationRecordArgs,
                            SigningJobRevocationRecordArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        signature_expires_at: Optional[pulumi.Input[_builtins.str]] = ...,
        signed_objects: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            SigningJobSignedObjectArgs, SigningJobSignedObjectArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        source: Optional[
            pulumi.Input[Union[SigningJobSourceArgs, SigningJobSourceArgsDict]]
        ] = ...,
        status: Optional[pulumi.Input[_builtins.str]] = ...,
        status_reason: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> SigningJob: ...
    @_builtins.property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def destination(self) -> pulumi.Output[outputs.SigningJobDestination]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreSigningJobFailure")
    def ignore_signing_job_failure(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobInvoker")
    def job_invoker(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="jobOwner")
    def job_owner(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestedBy")
    def requested_by(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(
        self,
    ) -> pulumi.Output[Sequence[outputs.SigningJobRevocationRecord]]: ...
    @_builtins.property
    @pulumi.getter(name="signatureExpiresAt")
    def signature_expires_at(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="signedObjects")
    def signed_objects(
        self,
    ) -> pulumi.Output[Sequence[outputs.SigningJobSignedObject]]: ...
    @_builtins.property
    @pulumi.getter
    def source(self) -> pulumi.Output[outputs.SigningJobSource]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[_builtins.str]: ...
