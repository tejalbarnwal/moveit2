from typing import Any

class LockedPlanningSceneContextManagerRO:
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type, value, traceback) -> Any: ...

class LockedPlanningSceneContextManagerRW:
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type, value, traceback) -> Any: ...

class MoveItPy:
    def __init__(self, *args, **kwargs) -> None: ...
    def execute(self, *args, **kwargs) -> Any: ...
    def get_planning_component(self, *args, **kwargs) -> Any: ...
    def get_planning_scene_monitor(self, *args, **kwargs) -> Any: ...
    def get_robot_model(self, *args, **kwargs) -> Any: ...
    def shutdown(self, *args, **kwargs) -> Any: ...

class MultiPipelinePlanRequestParameters:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def multi_plan_request_parameters(self) -> Any: ...

class PlanRequestParameters:
    max_acceleration_scaling_factor: Any
    max_velocity_scaling_factor: Any
    planner_id: Any
    planning_attempts: Any
    planning_pipeline: Any
    planning_time: Any
    def __init__(self, *args, **kwargs) -> None: ...

class PlanningComponent:
    def __init__(self, *args, **kwargs) -> None: ...
    def get_start_state(self, *args, **kwargs) -> Any: ...
    def plan(self, *args, **kwargs) -> Any: ...
    def set_goal_state(self, *args, **kwargs) -> Any: ...
    def set_path_constraints(self, *args, **kwargs) -> Any: ...
    def set_start_state(self, *args, **kwargs) -> Any: ...
    def set_start_state_to_current_state(self, *args, **kwargs) -> Any: ...
    def set_workspace(self, *args, **kwargs) -> Any: ...
    def unset_workspace(self, *args, **kwargs) -> Any: ...
    @property
    def named_target_state_values(self) -> Any: ...
    @property
    def named_target_states(self) -> Any: ...
    @property
    def planning_group_name(self) -> Any: ...

class PlanningSceneMonitor:
    def __init__(self, *args, **kwargs) -> None: ...
    def clear_octomap(self, *args, **kwargs) -> Any: ...
    def read_only(self, *args, **kwargs) -> Any: ...
    def read_write(self, *args, **kwargs) -> Any: ...
    def start_scene_monitor(self, *args, **kwargs) -> Any: ...
    def start_state_monitor(self, *args, **kwargs) -> Any: ...
    def stop_scene_monitor(self, *args, **kwargs) -> Any: ...
    def stop_state_monitor(self, *args, **kwargs) -> Any: ...
    def wait_for_current_robot_state(self, *args, **kwargs) -> Any: ...
    @property
    def name(self) -> Any: ...
