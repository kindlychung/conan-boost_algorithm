#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostAlgorithmConan(ConanFile):
    name = "boost_algorithm"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost_algorithm"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["algorithm"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.65.1@bincrafters/testing",
        "boost_array/1.65.1@bincrafters/testing",
        "boost_assert/1.65.1@bincrafters/testing",
        "boost_bind/1.65.1@bincrafters/testing",
        "boost_concept_check/1.65.1@bincrafters/testing",
        "boost_config/1.65.1@bincrafters/testing",
        "boost_core/1.65.1@bincrafters/testing",
        "boost_exception/1.65.1@bincrafters/testing",
        "boost_function/1.65.1@bincrafters/testing",
        "boost_iterator/1.65.1@bincrafters/testing",
        "boost_mpl/1.65.1@bincrafters/testing",
        "boost_range/1.65.1@bincrafters/testing",
        "boost_static_assert/1.65.1@bincrafters/testing",
        "boost_throw_exception/1.65.1@bincrafters/testing",
        "boost_tuple/1.65.1@bincrafters/testing",
        "boost_type_traits/1.65.1@bincrafters/testing",
        "boost_unordered/1.65.1@bincrafters/testing"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.65.1@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
