

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AiLogicConfigGenerativeLanguageConfig', 'AiLogicConfigTelemetryConfig', 'AppHostingBackendCodebase', 'AppHostingBackendManagedResource', 'AppHostingBackendManagedResourceRunService', 'AppHostingBuildError', 'AppHostingBuildSource', 'AppHostingBuildSourceCodebase', 'AppHostingBuildSourceCodebaseAuthor', 'AppHostingBuildSourceContainer', 'AppHostingDomainCustomDomainStatus', 'AppHostingDomainCustomDomainStatusIssue', ..., ..., ..., ..., ..., ..., ..., 'AppHostingDomainServe', 'AppHostingDomainServeRedirect', 'AppHostingTrafficCurrent', 'AppHostingTrafficCurrentSplit', 'AppHostingTrafficRolloutPolicy', 'AppHostingTrafficTarget', 'AppHostingTrafficTargetSplit', 'ExtensionsInstanceConfig', 'ExtensionsInstanceErrorStatus', 'ExtensionsInstanceRuntimeData', 'ExtensionsInstanceRuntimeDataFatalError', 'ExtensionsInstanceRuntimeDataProcessingState', 'HostingCustomDomainCert', 'HostingCustomDomainCertVerification', 'HostingCustomDomainCertVerificationDns', 'HostingCustomDomainCertVerificationDnsDesired', ..., 'HostingCustomDomainCertVerificationDnsDiscovered', ..., 'HostingCustomDomainCertVerificationHttp', 'HostingCustomDomainIssue', 'HostingCustomDomainRequiredDnsUpdate', 'HostingCustomDomainRequiredDnsUpdateDesired', 'HostingCustomDomainRequiredDnsUpdateDesiredRecord', 'HostingCustomDomainRequiredDnsUpdateDiscovered', ..., 'HostingVersionConfig', 'HostingVersionConfigHeader', 'HostingVersionConfigRedirect', 'HostingVersionConfigRewrite', 'HostingVersionConfigRewriteRun']
@pulumi.output_type
class AiLogicConfigGenerativeLanguageConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key: Optional[_builtins.str] = ..., api_key_wo: Optional[_builtins.str] = ..., api_key_wo_version: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyWo")
    def api_key_wo(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyWoVersion")
    def api_key_wo_version(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AiLogicConfigTelemetryConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, mode: Optional[_builtins.str] = ..., sampling_rate: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppHostingBackendCodebase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, repository: _builtins.str, root_directory: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootDirectory")
    def root_directory(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingBackendManagedResource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, run_services: Optional[Sequence[outputs.AppHostingBackendManagedResourceRunService]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="runServices")
    def run_services(self) -> Optional[Sequence[outputs.AppHostingBackendManagedResourceRunService]]:
        
        ...
    


@pulumi.output_type
class AppHostingBackendManagedResourceRunService(dict):
    def __init__(__self__, *, service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingBuildError(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[Mapping[str, _builtins.str]]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingBuildSource(dict):
    def __init__(__self__, *, codebase: Optional[outputs.AppHostingBuildSourceCodebase] = ..., container: Optional[outputs.AppHostingBuildSourceContainer] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def codebase(self) -> Optional[outputs.AppHostingBuildSourceCodebase]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def container(self) -> Optional[outputs.AppHostingBuildSourceContainer]:
        
        ...
    


@pulumi.output_type
class AppHostingBuildSourceCodebase(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, authors: Optional[Sequence[outputs.AppHostingBuildSourceCodebaseAuthor]] = ..., branch: Optional[_builtins.str] = ..., commit: Optional[_builtins.str] = ..., commit_message: Optional[_builtins.str] = ..., commit_time: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., hash: Optional[_builtins.str] = ..., uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def authors(self) -> Optional[Sequence[outputs.AppHostingBuildSourceCodebaseAuthor]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def commit(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitMessage")
    def commit_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="commitTime")
    def commit_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def hash(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingBuildSourceCodebaseAuthor(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., email: Optional[_builtins.str] = ..., image_uri: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def email(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingBuildSourceContainer(dict):
    def __init__(__self__, *, image: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatus(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert_state: Optional[_builtins.str] = ..., host_state: Optional[_builtins.str] = ..., issues: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusIssue]] = ..., ownership_state: Optional[_builtins.str] = ..., required_dns_updates: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdate]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="certState")
    def cert_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="hostState")
    def host_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def issues(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusIssue]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ownershipState")
    def ownership_state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredDnsUpdates")
    def required_dns_updates(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdate]]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusIssue(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, check_time: Optional[_builtins.str] = ..., desireds: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesired]] = ..., discovereds: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscovered]] = ..., domain_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def desireds(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesired]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def discovereds(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscovered]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesired(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, check_errors: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckError]] = ..., domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkErrors")
    def check_errors(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckError]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecord]]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredCheckError(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDesiredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., relevant_states: Optional[Sequence[_builtins.str]] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relevantStates")
    def relevant_states(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscovered(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, check_errors: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckError]] = ..., domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkErrors")
    def check_errors(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckError]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecord]]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredCheckError(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainCustomDomainStatusRequiredDnsUpdateDiscoveredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., relevant_states: Optional[Sequence[_builtins.str]] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relevantStates")
    def relevant_states(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainServe(dict):
    def __init__(__self__, *, redirect: Optional[outputs.AppHostingDomainServeRedirect] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirect(self) -> Optional[outputs.AppHostingDomainServeRedirect]:
        
        ...
    


@pulumi.output_type
class AppHostingDomainServeRedirect(dict):
    def __init__(__self__, *, uri: _builtins.str, status: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingTrafficCurrent(dict):
    def __init__(__self__, *, splits: Optional[Sequence[outputs.AppHostingTrafficCurrentSplit]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def splits(self) -> Optional[Sequence[outputs.AppHostingTrafficCurrentSplit]]:
        
        ...
    


@pulumi.output_type
class AppHostingTrafficCurrentSplit(dict):
    def __init__(__self__, *, build: Optional[_builtins.str] = ..., percent: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def build(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AppHostingTrafficRolloutPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, codebase_branch: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., disabled_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codebaseBranch")
    def codebase_branch(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disabledTime")
    def disabled_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppHostingTrafficTarget(dict):
    def __init__(__self__, *, splits: Sequence[outputs.AppHostingTrafficTargetSplit]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def splits(self) -> Sequence[outputs.AppHostingTrafficTargetSplit]:
        
        ...
    


@pulumi.output_type
class AppHostingTrafficTargetSplit(dict):
    def __init__(__self__, *, build: _builtins.str, percent: _builtins.int) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def build(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def percent(self) -> _builtins.int:
        
        ...
    


@pulumi.output_type
class ExtensionsInstanceConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, extension_ref: _builtins.str, params: Mapping[str, _builtins.str], allowed_event_types: Optional[Sequence[_builtins.str]] = ..., create_time: Optional[_builtins.str] = ..., eventarc_channel: Optional[_builtins.str] = ..., extension_version: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., populated_postinstall_content: Optional[_builtins.str] = ..., system_params: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionRef")
    def extension_ref(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def params(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedEventTypes")
    def allowed_event_types(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="eventarcChannel")
    def eventarc_channel(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="extensionVersion")
    def extension_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="populatedPostinstallContent")
    def populated_postinstall_content(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemParams")
    def system_params(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class ExtensionsInstanceErrorStatus(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[Sequence[Mapping[str, _builtins.str]]] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[Sequence[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtensionsInstanceRuntimeData(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fatal_error: Optional[outputs.ExtensionsInstanceRuntimeDataFatalError] = ..., processing_state: Optional[outputs.ExtensionsInstanceRuntimeDataProcessingState] = ..., state_update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fatalError")
    def fatal_error(self) -> Optional[outputs.ExtensionsInstanceRuntimeDataFatalError]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processingState")
    def processing_state(self) -> Optional[outputs.ExtensionsInstanceRuntimeDataProcessingState]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="stateUpdateTime")
    def state_update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtensionsInstanceRuntimeDataFatalError(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, error_message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExtensionsInstanceRuntimeDataProcessingState(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, detail_message: Optional[_builtins.str] = ..., state: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detailMessage")
    def detail_message(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCert(dict):
    def __init__(__self__, *, state: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ..., verification: Optional[outputs.HostingCustomDomainCertVerification] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def verification(self) -> Optional[outputs.HostingCustomDomainCertVerification]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerification(dict):
    def __init__(__self__, *, dns: Optional[outputs.HostingCustomDomainCertVerificationDns] = ..., http: Optional[outputs.HostingCustomDomainCertVerificationHttp] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dns(self) -> Optional[outputs.HostingCustomDomainCertVerificationDns]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def http(self) -> Optional[outputs.HostingCustomDomainCertVerificationHttp]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationDns(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, check_time: Optional[_builtins.str] = ..., desireds: Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDesired]] = ..., discovereds: Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDiscovered]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def desireds(self) -> Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDesired]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def discovereds(self) -> Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDiscovered]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationDnsDesired(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDesiredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDesiredRecord]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationDnsDesiredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationDnsDiscovered(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDiscoveredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.HostingCustomDomainCertVerificationDnsDiscoveredRecord]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationDnsDiscoveredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainCertVerificationHttp(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, desired: Optional[_builtins.str] = ..., discovered: Optional[_builtins.str] = ..., last_check_time: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def desired(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def discovered(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastCheckTime")
    def last_check_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainIssue(dict):
    def __init__(__self__, *, code: Optional[_builtins.int] = ..., details: Optional[_builtins.str] = ..., message: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainRequiredDnsUpdate(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, check_time: Optional[_builtins.str] = ..., desireds: Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDesired]] = ..., discovereds: Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDiscovered]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="checkTime")
    def check_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def desireds(self) -> Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDesired]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def discovereds(self) -> Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDiscovered]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainRequiredDnsUpdateDesired(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDesiredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDesiredRecord]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainRequiredDnsUpdateDesiredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainRequiredDnsUpdateDiscovered(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., records: Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDiscoveredRecord]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def records(self) -> Optional[Sequence[outputs.HostingCustomDomainRequiredDnsUpdateDiscoveredRecord]]:
        
        ...
    


@pulumi.output_type
class HostingCustomDomainRequiredDnsUpdateDiscoveredRecord(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, domain_name: Optional[_builtins.str] = ..., rdata: Optional[_builtins.str] = ..., required_action: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rdata(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requiredAction")
    def required_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingVersionConfig(dict):
    def __init__(__self__, *, headers: Optional[Sequence[outputs.HostingVersionConfigHeader]] = ..., redirects: Optional[Sequence[outputs.HostingVersionConfigRedirect]] = ..., rewrites: Optional[Sequence[outputs.HostingVersionConfigRewrite]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[outputs.HostingVersionConfigHeader]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def redirects(self) -> Optional[Sequence[outputs.HostingVersionConfigRedirect]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def rewrites(self) -> Optional[Sequence[outputs.HostingVersionConfigRewrite]]:
        
        ...
    


@pulumi.output_type
class HostingVersionConfigHeader(dict):
    def __init__(__self__, *, headers: Mapping[str, _builtins.str], glob: Optional[_builtins.str] = ..., regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def headers(self) -> Mapping[str, _builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingVersionConfigRedirect(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, location: _builtins.str, status_code: _builtins.int, glob: Optional[_builtins.str] = ..., regex: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> _builtins.int:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class HostingVersionConfigRewrite(dict):
    def __init__(__self__, *, function: Optional[_builtins.str] = ..., glob: Optional[_builtins.str] = ..., path: Optional[_builtins.str] = ..., regex: Optional[_builtins.str] = ..., run: Optional[outputs.HostingVersionConfigRewriteRun] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def function(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def glob(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def regex(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def run(self) -> Optional[outputs.HostingVersionConfigRewriteRun]:
        
        ...
    


@pulumi.output_type
class HostingVersionConfigRewriteRun(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_id: _builtins.str, region: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[_builtins.str]:
        
        ...
    


