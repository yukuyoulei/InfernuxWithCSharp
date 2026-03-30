#pragma once

/**
 * @file InxPlatform.h
 * @brief Centralised platform detection and Windows header isolation.
 *
 * Include this header instead of <windows.h> anywhere in the engine.
 * It guarantees:
 *   - NOMINMAX is defined before windows.h (prevents min/max macro conflicts)
 *   - WIN32_LEAN_AND_MEAN is defined (reduces windows.h bloat)
 *   - Platform macros INX_PLATFORM_WINDOWS / LINUX / MACOS / ANDROID
 *
 * Usage:
 *   #include <core/config/InxPlatform.h>
 */

// ── Platform detection ────────────────────────────────────────────────────────
#if defined(_WIN32) || defined(_WIN64)
#define INX_PLATFORM_WINDOWS 1
#elif defined(__ANDROID__)
#define INX_PLATFORM_ANDROID 1
#elif defined(__linux__)
#define INX_PLATFORM_LINUX 1
#elif defined(__APPLE__)
#include <TargetConditionals.h>
#if TARGET_OS_IPHONE
#define INX_PLATFORM_IOS 1
#else
#define INX_PLATFORM_MACOS 1
#endif
#endif

// ── Windows header configuration ──────────────────────────────────────────────
#ifdef INX_PLATFORM_WINDOWS
#ifndef NOMINMAX
#define NOMINMAX
#endif
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif
#include <windows.h>
#endif
