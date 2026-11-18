import sys
import os

# Ensure backend directory is in Python path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    from backend.ai.agent import IntelligentAgent
    agent = IntelligentAgent(size=8)
    print("✓ Import and agent initialization successful: safe to push.")
except Exception as e:
    print(f"✗ Verification failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

