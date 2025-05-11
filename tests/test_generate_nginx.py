import subprocess
import sys

def test_help_shows_description():
    """Running generate_nginx --help should exit 0 and print usage."""
    result = subprocess.run([sys.executable, "-m", "generate_nginx", "--help"],
                            capture_output=True, text=True)
    assert result.returncode == 0
    assert "usage:" in result.stdout.lower()
    assert "generate_nginx" in result.stdout
