include(CMakeFindDependencyMacro)
find_dependency(Protobuf CONFIG)
include("${CMAKE_CURRENT_LIST_DIR}/ht_protoTargets.cmake")