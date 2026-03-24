

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['RoutineArgs', 'Routine']
@pulumi.input_type
class RoutineArgs:
    def __init__(__self__, *, dataset_id: pulumi.Input[_builtins.str], definition_body: pulumi.Input[_builtins.str], routine_id: pulumi.Input[_builtins.str], routine_type: pulumi.Input[_builtins.str], arguments: Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]] = ..., data_governance_type: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., determinism_level: Optional[pulumi.Input[_builtins.str]] = ..., external_runtime_options: Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]] = ..., imported_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_options: Optional[pulumi.Input[RoutinePythonOptionsArgs]] = ..., remote_function_options: Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]] = ..., return_table_type: Optional[pulumi.Input[_builtins.str]] = ..., return_type: Optional[pulumi.Input[_builtins.str]] = ..., security_mode: Optional[pulumi.Input[_builtins.str]] = ..., spark_options: Optional[pulumi.Input[RoutineSparkOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @dataset_id.setter
    def dataset_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionBody")
    def definition_body(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @definition_body.setter
    def definition_body(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @routine_id.setter
    def routine_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineType")
    def routine_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @routine_type.setter
    def routine_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]]:
        
        ...
    
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataGovernanceType")
    def data_governance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_governance_type.setter
    def data_governance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="determinismLevel")
    def determinism_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @determinism_level.setter
    def determinism_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalRuntimeOptions")
    def external_runtime_options(self) -> Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]]:
        
        ...
    
    @external_runtime_options.setter
    def external_runtime_options(self, value: Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importedLibraries")
    def imported_libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @imported_libraries.setter
    def imported_libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonOptions")
    def python_options(self) -> Optional[pulumi.Input[RoutinePythonOptionsArgs]]:
        
        ...
    
    @python_options.setter
    def python_options(self, value: Optional[pulumi.Input[RoutinePythonOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteFunctionOptions")
    def remote_function_options(self) -> Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]]:
        
        ...
    
    @remote_function_options.setter
    def remote_function_options(self, value: Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnTableType")
    def return_table_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @return_table_type.setter
    def return_table_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnType")
    def return_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @return_type.setter
    def return_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityMode")
    def security_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_mode.setter
    def security_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkOptions")
    def spark_options(self) -> Optional[pulumi.Input[RoutineSparkOptionsArgs]]:
        
        ...
    
    @spark_options.setter
    def spark_options(self, value: Optional[pulumi.Input[RoutineSparkOptionsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _RoutineState:
    def __init__(__self__, *, arguments: Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]] = ..., creation_time: Optional[pulumi.Input[_builtins.int]] = ..., data_governance_type: Optional[pulumi.Input[_builtins.str]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., definition_body: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., determinism_level: Optional[pulumi.Input[_builtins.str]] = ..., external_runtime_options: Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]] = ..., imported_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_options: Optional[pulumi.Input[RoutinePythonOptionsArgs]] = ..., remote_function_options: Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]] = ..., return_table_type: Optional[pulumi.Input[_builtins.str]] = ..., return_type: Optional[pulumi.Input[_builtins.str]] = ..., routine_id: Optional[pulumi.Input[_builtins.str]] = ..., routine_type: Optional[pulumi.Input[_builtins.str]] = ..., security_mode: Optional[pulumi.Input[_builtins.str]] = ..., spark_options: Optional[pulumi.Input[RoutineSparkOptionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]]:
        
        ...
    
    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[RoutineArgumentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataGovernanceType")
    def data_governance_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_governance_type.setter
    def data_governance_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @dataset_id.setter
    def dataset_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionBody")
    def definition_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @definition_body.setter
    def definition_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="determinismLevel")
    def determinism_level(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @determinism_level.setter
    def determinism_level(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalRuntimeOptions")
    def external_runtime_options(self) -> Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]]:
        
        ...
    
    @external_runtime_options.setter
    def external_runtime_options(self, value: Optional[pulumi.Input[RoutineExternalRuntimeOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="importedLibraries")
    def imported_libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @imported_libraries.setter
    def imported_libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language.setter
    def language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @last_modified_time.setter
    def last_modified_time(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonOptions")
    def python_options(self) -> Optional[pulumi.Input[RoutinePythonOptionsArgs]]:
        
        ...
    
    @python_options.setter
    def python_options(self, value: Optional[pulumi.Input[RoutinePythonOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteFunctionOptions")
    def remote_function_options(self) -> Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]]:
        
        ...
    
    @remote_function_options.setter
    def remote_function_options(self, value: Optional[pulumi.Input[RoutineRemoteFunctionOptionsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnTableType")
    def return_table_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @return_table_type.setter
    def return_table_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnType")
    def return_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @return_type.setter
    def return_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routine_id.setter
    def routine_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineType")
    def routine_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @routine_type.setter
    def routine_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityMode")
    def security_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_mode.setter
    def security_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkOptions")
    def spark_options(self) -> Optional[pulumi.Input[RoutineSparkOptionsArgs]]:
        
        ...
    
    @spark_options.setter
    def spark_options(self, value: Optional[pulumi.Input[RoutineSparkOptionsArgs]]): # -> None:
        ...
    


@pulumi.type_token("gcp:bigquery/routine:Routine")
class Routine(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., arguments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoutineArgumentArgs, RoutineArgumentArgsDict]]]]] = ..., data_governance_type: Optional[pulumi.Input[_builtins.str]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., definition_body: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., determinism_level: Optional[pulumi.Input[_builtins.str]] = ..., external_runtime_options: Optional[pulumi.Input[Union[RoutineExternalRuntimeOptionsArgs, RoutineExternalRuntimeOptionsArgsDict]]] = ..., imported_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_options: Optional[pulumi.Input[Union[RoutinePythonOptionsArgs, RoutinePythonOptionsArgsDict]]] = ..., remote_function_options: Optional[pulumi.Input[Union[RoutineRemoteFunctionOptionsArgs, RoutineRemoteFunctionOptionsArgsDict]]] = ..., return_table_type: Optional[pulumi.Input[_builtins.str]] = ..., return_type: Optional[pulumi.Input[_builtins.str]] = ..., routine_id: Optional[pulumi.Input[_builtins.str]] = ..., routine_type: Optional[pulumi.Input[_builtins.str]] = ..., security_mode: Optional[pulumi.Input[_builtins.str]] = ..., spark_options: Optional[pulumi.Input[Union[RoutineSparkOptionsArgs, RoutineSparkOptionsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: RoutineArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., arguments: Optional[pulumi.Input[Sequence[pulumi.Input[Union[RoutineArgumentArgs, RoutineArgumentArgsDict]]]]] = ..., creation_time: Optional[pulumi.Input[_builtins.int]] = ..., data_governance_type: Optional[pulumi.Input[_builtins.str]] = ..., dataset_id: Optional[pulumi.Input[_builtins.str]] = ..., definition_body: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., determinism_level: Optional[pulumi.Input[_builtins.str]] = ..., external_runtime_options: Optional[pulumi.Input[Union[RoutineExternalRuntimeOptionsArgs, RoutineExternalRuntimeOptionsArgsDict]]] = ..., imported_libraries: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., language: Optional[pulumi.Input[_builtins.str]] = ..., last_modified_time: Optional[pulumi.Input[_builtins.int]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., python_options: Optional[pulumi.Input[Union[RoutinePythonOptionsArgs, RoutinePythonOptionsArgsDict]]] = ..., remote_function_options: Optional[pulumi.Input[Union[RoutineRemoteFunctionOptionsArgs, RoutineRemoteFunctionOptionsArgsDict]]] = ..., return_table_type: Optional[pulumi.Input[_builtins.str]] = ..., return_type: Optional[pulumi.Input[_builtins.str]] = ..., routine_id: Optional[pulumi.Input[_builtins.str]] = ..., routine_type: Optional[pulumi.Input[_builtins.str]] = ..., security_mode: Optional[pulumi.Input[_builtins.str]] = ..., spark_options: Optional[pulumi.Input[Union[RoutineSparkOptionsArgs, RoutineSparkOptionsArgsDict]]] = ...) -> Routine:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arguments(self) -> pulumi.Output[Optional[Sequence[outputs.RoutineArgument]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataGovernanceType")
    def data_governance_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="datasetId")
    def dataset_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="definitionBody")
    def definition_body(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="determinismLevel")
    def determinism_level(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="externalRuntimeOptions")
    def external_runtime_options(self) -> pulumi.Output[Optional[outputs.RoutineExternalRuntimeOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="importedLibraries")
    def imported_libraries(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def language(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonOptions")
    def python_options(self) -> pulumi.Output[Optional[outputs.RoutinePythonOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteFunctionOptions")
    def remote_function_options(self) -> pulumi.Output[Optional[outputs.RoutineRemoteFunctionOptions]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnTableType")
    def return_table_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnType")
    def return_type(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineId")
    def routine_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routineType")
    def routine_type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securityMode")
    def security_mode(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sparkOptions")
    def spark_options(self) -> pulumi.Output[Optional[outputs.RoutineSparkOptions]]:
        
        ...
    


