from pathlib import Path


def test_expected_project_directories_exist() -> None:
    expected_dirs = [
        "app",
        "src",
        "data",
        "docs",
        "evals",
        "tests",
        "vector_store/chroma",
    ]

    for directory in expected_dirs:
        assert Path(directory).is_dir(), f"Missing expected directory: {directory}"
