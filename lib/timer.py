from typing import Callable, TypeVar, Any, List
import time
from dataclasses import dataclass


@dataclass
class TimedRun:
    index: int
    seconds: float


@dataclass
class BatchRun:
    runs: list[TimedRun]
    average: float
    minimum: float
    maximum: float


# Define a generic type for the return value of the function
R = TypeVar("R")


def timer(func: Callable[..., R], *args: Any, **kwargs: Any) -> TimedRun:
    """
    Times the execution of a given function with any number of arguments and keyword arguments.

    Args:
        func (Callable[..., R]): The function to be timed.
        *args (Any): Positional arguments for the function.
        **kwargs (Any): Keyword arguments for the function.

    Returns:
        Time in seconds (float)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    return TimedRun(0, elapsed_time)


def batch_timer(
    func: Callable[..., R], num_runs: int, *args: Any, **kwargs: Any
) -> BatchRun:
    """
    Times the execution of a given function over multiple runs and computes the average time.

    Args:
        func (Callable[..., R]): The function to be timed.
        num_runs (int): Number of times to execute the function.
        *args (Any): Positional arguments for the function.
        **kwargs (Any): Keyword arguments for the function.

    Returns:
        tuple[float, List[float]]: A tuple containing:
            - The average time in seconds (float)
            - A list of times for each run (List[float])
    """
    times = []  # List to store the time for each run
    runs = []
    idx = 0
    for _ in range(num_runs):
        idx += 1
        print(f"Batch job {idx}/{num_runs}...", end="\r")
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        runs.append(TimedRun(idx, elapsed_time))
        times.append(elapsed_time)
    print("                                           ", end="\r")
    average_time = sum(times) / num_runs
    min_time = min(times)
    max_time = max(times)

    return BatchRun(runs=runs, average=average_time, minimum=min_time, maximum=max_time)
