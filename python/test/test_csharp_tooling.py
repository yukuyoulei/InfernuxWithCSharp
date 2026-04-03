from __future__ import annotations

from pathlib import Path

from Infernux.engine.csharp_tooling import CSHARP_STUBS_FILE, ensure_csharp_tooling


def test_generated_runtime_stubs_include_extended_transform_bridge(tmp_path: Path):
    ensure_csharp_tooling(str(tmp_path), project_name="BridgeTest")

    stubs_path = tmp_path / CSHARP_STUBS_FILE
    content = stubs_path.read_text(encoding="utf-8")

    assert "public readonly struct Quaternion" in content
    assert "public Quaternion rotation" in content
    assert "public Quaternion localRotation" in content
    assert "public Vector3 eulerAngles" in content
    assert "public Vector3 localEulerAngles" in content
    assert "public Vector3 lossyScale => Managed.NativeApi.GetWorldScale(_gameObject.InstanceId);" in content
    assert "public Transform root" in content
    assert "public Vector3 forward => rotation * ForwardAxis;" in content
    assert "public void TranslateLocal(Vector3 delta)" in content
    assert "public void Rotate(Vector3 eulerAngles)" in content
    assert "public void Rotate(Vector3 axis, float angle)" in content
    assert "public void RotateAround(Vector3 point, Vector3 axis, float angle)" in content
    assert "public void LookAt(Vector3 target)" in content
    assert "public Vector3 TransformPoint(Vector3 point)" in content
    assert "public Vector3 InverseTransformDirection(Vector3 direction)" in content
    assert "public bool IsChildOf(Transform? parent)" in content
    assert "public void DetachChildren()" in content
    assert "public int GetSiblingIndex()" in content
    assert "public void SetAsLastSibling()" in content
    assert "private delegate int GetWorldRotationDelegate" in content
    assert "private delegate int GetWorldEulerAnglesDelegate" in content
    assert "private delegate int TranslateLocalDelegate" in content
    assert "private delegate int RotateAroundDelegate" in content
    assert "private delegate int TransformVectorDelegate" in content
    assert "private delegate int SetSiblingIndexDelegate" in content
    assert "private delegate int DetachChildrenDelegate" in content
