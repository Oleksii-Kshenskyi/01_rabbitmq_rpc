#pragma once
#include <cstdint>

#if defined(_MSC_VER)
    //  Microsoft 
    #define EXPORT extern "C" __declspec(dllexport)
    #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    //  GCC
    #define EXPORT extern "C" __attribute__((visibility("default")))
    #define IMPORT
#else
    //  do nothing and hope for the best?
    #define EXPORT extern "C"
    #define IMPORT
    #pragma warning Unknown dynamic link import/export semantics.
#endif

EXPORT uint64_t sum_ints(uint32_t one, uint32_t two);
EXPORT uint64_t mul_ints(uint32_t one, uint32_t two);