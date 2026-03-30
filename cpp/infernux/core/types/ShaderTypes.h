#pragma once

namespace infernux
{

// ============================================================================
// ShaderCompileTarget — identifies which rendering pass variant to compile for.
//
// Shared between InxShaderLoader (compile-time variant generation) and
// InxMaterial (per-pass pipeline storage).  Defined in a lightweight header
// to avoid pulling in heavy shader-compiler includes through InxMaterial.h.
// ============================================================================

enum class ShaderCompileTarget : int
{
    Forward = 0, // Standard forward rendering (default)
    GBuffer = 1, // Deferred GBuffer output
    Shadow = 2,  // Depth-only shadow caster

    Count // Sentinel — number of targets; must be last
};

} // namespace infernux
