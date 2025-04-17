
from setuptools import setup, find_packages

setup(
    name="payment-powerful-platform",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Payment service implementing FastAPI and Celery architecture",
    keywords="payment-powerful-platform, python",
    url="",
)
