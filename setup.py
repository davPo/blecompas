from setuptools import setup

setup(name='ble_compass',
      version='0.1',
      description='3D compensated compass with BLE interface',
      url='https://github.com/davPo/ble_compas.git',
      author='Dpo',
  #    author_email='flyingcircus@example.com',
      license='GNU GPLv3',
      packages=['blecompas'],
        install_requires=[
          'bleak',
      ],
      zip_safe=False)