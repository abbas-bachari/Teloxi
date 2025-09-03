from setuptools import setup, find_packages



setup(
    name='teloxi',
    version='1.0.0',
    author='Abbas Bachari',
    author_email='abbas-bachari@hotmail.com',
    description='A user-friendly library based on Telethon, with additional features and easier usage.',
    long_description=open('README.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/abbas-bachari/teloxi',
    python_requires='>=3.10',
    project_urls={
    "Homepage"      :'https://github.com/abbas-bachari/teloxi',
    'Documentation' : 'https://github.com/abbas-bachari/teloxi',
    'Source'        : 'https://github.com/abbas-bachari/teloxi/',
    'Tracker'       : 'https://github.com/abbas-bachari/teloxi/issues',
   
},
    
    install_requires=[
        "loguru",
        "dbflux",
        "telethon",
        "python-socks[asyncio]"
        ],
    
    keywords=[
        'telethon','telegram',
        'telegram multi session', 
        'telegram-python', 'opentele', 
        'openetele','teloxi' , 'dbflux',
        'api', 'abbas bachari',"عباس بچاری"],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
       
    ],
)


