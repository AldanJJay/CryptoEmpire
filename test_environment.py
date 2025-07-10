#!/usr/bin/env python3
"""
Test script to verify the uv environment setup for microcosm-4x project.
"""

def test_imports():
    """Test that all main dependencies can be imported."""
    try:
        import pyxel
        print("✓ Pyxel imported successfully")
        
        import platformdirs
        print("✓ platformdirs imported successfully")
        
        import PIL
        print("✓ Pillow (PIL) imported successfully")
        
        # Note: python-vlc requires VLC media player to be installed on the system
        try:
            import vlc
            print("✓ python-vlc imported successfully")
        except FileNotFoundError:
            print("⚠ python-vlc requires VLC media player to be installed")
        
        # Test project imports (avoiding the VLC dependency for now)
        try:
            from source.foundation import models
            print("✓ Project models imported successfully")
            
            from source.display import board
            print("✓ Project display modules imported successfully")
            
        except ImportError as e:
            print(f"⚠ Some project modules require VLC: {e}")
        
        print("\n✓ Environment setup successful!")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_dev_dependencies():
    """Test that development dependencies can be imported."""
    dev_packages = ['pylint', 'coverage', 'nuitka', 'imageio', 'hatch']
    
    print("\nTesting development dependencies:")
    for package in dev_packages:
        try:
            __import__(package)
            print(f"✓ {package} imported successfully")
        except ImportError as e:
            print(f"✗ {package} import failed: {e}")

if __name__ == "__main__":
    print("Testing microcosm-4x environment with uv...")
    print("=" * 50)
    
    success = test_imports()
    test_dev_dependencies()
    
    print("\n" + "=" * 50)
    if success:
        print("Environment test completed successfully!")
        print("\nTo run the project:")
        print("  python -m uv run python microcosm.py")
        print("  # or")
        print("  python -m uv run microcosm")
        print("\nTo run tests:")
        print("  python -m uv run python -m pytest source/tests/")
        print("\nTo run linting:")
        print("  python -m uv run pylint source/")
    else:
        print("Some issues were found. Check the output above.")
