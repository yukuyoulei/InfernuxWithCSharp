#pragma once

#include "InxGUIContext.h"

#include <core/log/InxLog.h>

namespace infernux
{
class InxGUIRenderable
{
  public:
    virtual ~InxGUIRenderable() = default;
    virtual void OnRender(InxGUIContext *ctx)
    {
        INXLOG_FATAL("InxGUIRenderable::OnRender not implemented");
    }
};
} // namespace infernux