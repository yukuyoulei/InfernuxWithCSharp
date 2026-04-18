from __future__ import annotations

from pathlib import Path

from Infernux.engine.csharp_tooling import CSHARP_STUBS_FILE, ensure_csharp_tooling


def test_generated_runtime_stubs_include_extended_transform_bridge(tmp_path: Path):
    ensure_csharp_tooling(str(tmp_path), project_name="BridgeTest")

    stubs_path = tmp_path / CSHARP_STUBS_FILE
    content = stubs_path.read_text(encoding="utf-8")

    assert "public enum CameraProjection" in content
    assert "public enum CameraClearFlags" in content
    assert "public readonly struct Vector2" in content
    assert "public readonly struct Quaternion" in content
    assert "public struct Color" in content
    assert "public struct Color32" in content
    assert "public struct Matrix4x4" in content
    assert "public struct Ray" in content
    assert "public static class Mathf" in content
    assert "public static class Random" in content
    assert "public enum Space" in content
    assert "public abstract class Object" in content
    assert "public abstract class Component : Object" in content
    assert "public abstract class Behaviour : Component" in content
    assert "public sealed class Camera : Behaviour" in content
    assert "public sealed class Transform : Component" in content
    assert "public abstract class MonoBehaviour : Behaviour" in content
    assert "public abstract class InxComponent : MonoBehaviour" not in content
    assert "public abstract long GetInstanceID();" in content
    assert "public static T? Instantiate<T>(T original) where T : Object" in content
    assert "public static void Destroy(Object? obj)" in content
    assert "public Quaternion rotation" in content
    assert "public Quaternion localRotation" in content
    assert "public Vector3 eulerAngles" in content
    assert "public Vector3 localEulerAngles" in content
    assert "public Vector3 lossyScale => Managed.NativeApi.GetWorldScale(_gameObject.InstanceId);" in content
    assert "public Matrix4x4 localToWorldMatrix => Matrix4x4.TRS(position, rotation, lossyScale);" in content
    assert "public Matrix4x4 worldToLocalMatrix => localToWorldMatrix.inverse;" in content
    assert "public Transform root" in content
    assert "public bool hasChanged" in content
    assert "public static Camera? main => Managed.ManagedComponentBridge.GetMainCamera();" in content
    assert "public CameraProjection projectionMode" in content
    assert "public bool orthographic" in content
    assert "public float fieldOfView" in content
    assert "public float aspect" in content
    assert "public float nearClipPlane" in content
    assert "public float farClipPlane" in content
    assert "public int cullingMask" in content
    assert "public CameraClearFlags clearFlags" in content
    assert "public Color backgroundColor" in content
    assert "public Vector3 ScreenToWorldPoint(Vector3 position)" in content
    assert "public Vector3 WorldToScreenPoint(Vector3 position)" in content
    assert "public Ray ScreenPointToRay(Vector2 position)" in content
    assert "get => rotation * ForwardAxis;" in content
    assert "get => rotation * RightAxis;" in content
    assert "get => rotation * UpAxis;" in content
    assert "rotation = Quaternion.LookRotation(value, up);" in content
    assert "Vector3 targetForward = Vector3.Cross(value.normalized, targetUp).normalized;" in content
    assert "rotation = Quaternion.LookRotation(forward, value);" in content
    assert "public void SetPositionAndRotation(Vector3 position, Quaternion rotation)" in content
    assert "public void GetPositionAndRotation(out Vector3 position, out Quaternion rotation)" in content
    assert "public void SetLocalPositionAndRotation(Vector3 localPosition, Quaternion localRotation)" in content
    assert "public void GetLocalPositionAndRotation(out Vector3 localPosition, out Quaternion localRotation)" in content
    assert "public void Translate(Vector3 translation, Space relativeTo = Space.Self)" in content
    assert "public void Translate(float x, float y, float z)" in content
    assert "public void Translate(float x, float y, float z, Space relativeTo = Space.Self)" in content
    assert "public void Translate(Vector3 translation, Transform? relativeTo)" in content
    assert "public void Translate(float x, float y, float z, Transform? relativeTo)" in content
    assert "public void TranslateLocal(Vector3 delta)" in content
    assert "public void Rotate(Vector3 eulerAngles)" in content
    assert "public void Rotate(Vector3 eulerAngles, Space relativeTo = Space.Self)" in content
    assert "public void Rotate(float xAngle, float yAngle, float zAngle)" in content
    assert "public void Rotate(float xAngle, float yAngle, float zAngle, Space relativeTo = Space.Self)" in content
    assert "public void Rotate(Vector3 axis, float angle)" in content
    assert "public void Rotate(Vector3 axis, float angle, Space relativeTo)" in content
    assert "public void RotateAround(Vector3 point, Vector3 axis, float angle)" in content
    assert "public void LookAt(Vector3 target)" in content
    assert "public void LookAt(Transform target)" in content
    assert "public void LookAt(Transform target, Vector3 worldUp)" in content
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
    assert "private delegate int GetTransformHasChangedDelegate(long gameObjectId, out int hasChanged);" in content
    assert "private delegate int SetTransformHasChangedDelegate(long gameObjectId, int hasChanged);" in content
    assert "private delegate int GetComponentEnabledDelegate(long componentId, out int enabled);" in content
    assert "private delegate long AddCameraComponentDelegate(long gameObjectId);" in content
    assert "private delegate long GetCameraComponentIdDelegate(long gameObjectId);" in content
    assert "private delegate long GetMainCameraGameObjectIdDelegate();" in content
    assert "private delegate int GetCameraProjectionModeDelegate(long componentId, out int mode);" in content
    assert "private delegate int CameraScreenPointToRayDelegate(" in content
    assert "public T? AddComponent<T>() where T : MonoBehaviour" in content
    assert "public Component? AddComponent(Type type)" in content
    assert "public T? GetComponent<T>() where T : Component" in content
    assert "public Component? GetComponent(Type type)" in content
    assert "public bool TryGetComponent<T>(out T? component) where T : Component" in content
    assert "public bool TryGetComponent(Type type, out Component? component)" in content
    assert "public T[] GetComponents<T>() where T : Component" in content
    assert "public void GetComponents<T>(List<T> results) where T : Component" in content
    assert "public Component[] GetComponents(Type type)" in content
    assert "public void GetComponents(Type type, List<Component> results)" in content
    assert "public T? GetComponentInChildren<T>() where T : Component" in content
    assert "public T? GetComponentInChildren<T>(bool includeInactive) where T : Component" in content
    assert "public bool TryGetComponentInChildren<T>(out T? component) where T : Component" in content
    assert "public bool TryGetComponentInChildren<T>(bool includeInactive, out T? component) where T : Component" in content
    assert "public Component? GetComponentInChildren(Type type)" in content
    assert "public Component? GetComponentInChildren(Type type, bool includeInactive)" in content
    assert "public bool TryGetComponentInChildren(Type type, out Component? component)" in content
    assert "public bool TryGetComponentInChildren(Type type, bool includeInactive, out Component? component)" in content
    assert "public T[] GetComponentsInChildren<T>() where T : Component" in content
    assert "public T[] GetComponentsInChildren<T>(bool includeInactive) where T : Component" in content
    assert "public void GetComponentsInChildren<T>(List<T> results) where T : Component" in content
    assert "public void GetComponentsInChildren<T>(bool includeInactive, List<T> results) where T : Component" in content
    assert "public Component[] GetComponentsInChildren(Type type)" in content
    assert "public Component[] GetComponentsInChildren(Type type, bool includeInactive)" in content
    assert "public void GetComponentsInChildren(Type type, List<Component> results)" in content
    assert "public void GetComponentsInChildren(Type type, bool includeInactive, List<Component> results)" in content
    assert "public T? GetComponentInParent<T>() where T : Component" in content
    assert "public T? GetComponentInParent<T>(bool includeInactive) where T : Component" in content
    assert "public bool TryGetComponentInParent<T>(out T? component) where T : Component" in content
    assert "public bool TryGetComponentInParent<T>(bool includeInactive, out T? component) where T : Component" in content
    assert "public Component? GetComponentInParent(Type type)" in content
    assert "public Component? GetComponentInParent(Type type, bool includeInactive)" in content
    assert "public bool TryGetComponentInParent(Type type, out Component? component)" in content
    assert "public bool TryGetComponentInParent(Type type, bool includeInactive, out Component? component)" in content
    assert "public T[] GetComponentsInParent<T>() where T : Component" in content
    assert "public T[] GetComponentsInParent<T>(bool includeInactive) where T : Component" in content
    assert "public void GetComponentsInParent<T>(List<T> results) where T : Component" in content
    assert "public void GetComponentsInParent<T>(bool includeInactive, List<T> results) where T : Component" in content
    assert "public Component[] GetComponentsInParent(Type type)" in content
    assert "public Component[] GetComponentsInParent(Type type, bool includeInactive)" in content
    assert "public void GetComponentsInParent(Type type, List<Component> results)" in content
    assert "public void GetComponentsInParent(Type type, bool includeInactive, List<Component> results)" in content
    assert "public override string name" in content
    assert "public bool CompareTag(string tag)" in content
    assert "public abstract bool enabled { get; set; }" in content
    assert "public bool isActiveAndEnabled => enabled && (gameObject?.activeInHierarchy ?? false);" in content
    assert "public override long GetInstanceID()" in content
    assert "return Managed.NativeApi.GetTransformComponentId(_gameObject.InstanceId);" in content
    assert "Managed.NativeApi.SetComponentEnabled(ComponentId, value);" in content
    assert "private delegate long AddManagedComponentDelegate" in content
    assert "private delegate long GetManagedComponentDelegate" in content
    assert "private delegate long GetManagedComponentInChildrenDelegate" in content
    assert "private delegate long GetManagedComponentInParentDelegate" in content
    assert "private delegate long GetTransformComponentIdDelegate(long gameObjectId);" in content
    assert "private delegate int SetComponentEnabledDelegate(long componentId, int enabled);" in content
    assert "private delegate int DestroyComponentByIdDelegate(long componentId);" in content
    assert "internal static string GetManagedTypeName<T>() where T : MonoBehaviour" in content
    assert "internal static T? GetManagedComponent<T>(long handle) where T : MonoBehaviour" in content
    assert "private static readonly Dictionary<long, MonoBehaviour> Components = new();" in content
    assert "internal static T? InstantiateObject<T>(T original, Transform? parent) where T : Object" in content
    assert "internal static Component? AddGameObjectComponent(GameObject gameObject, Type type)" in content
    assert "internal static T? GetGameObjectComponent<T>(GameObject gameObject) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponent<T>(GameObject gameObject, out T? component) where T : Component" in content
    assert "internal static T[] GetGameObjectComponents<T>(GameObject gameObject) where T : Component" in content
    assert "internal static void GetGameObjectComponents<T>(GameObject gameObject, List<T> results) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponent(GameObject gameObject, Type type, out Component? component)" in content
    assert "internal static Component[] GetGameObjectComponents(GameObject gameObject, Type type)" in content
    assert "internal static void GetGameObjectComponents(GameObject gameObject, Type type, List<Component> results)" in content
    assert "internal static T[] GetGameObjectComponentsInChildren<T>(GameObject gameObject) where T : Component" in content
    assert "internal static T[] GetGameObjectComponentsInChildren<T>(GameObject gameObject, bool includeInactive) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponentInChildren<T>(GameObject gameObject, out T? component) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponentInChildren<T>(GameObject gameObject, bool includeInactive, out T? component) where T : Component" in content
    assert "internal static void GetGameObjectComponentsInChildren<T>(GameObject gameObject, List<T> results) where T : Component" in content
    assert "internal static void GetGameObjectComponentsInChildren<T>(GameObject gameObject, bool includeInactive, List<T> results) where T : Component" in content
    assert "internal static Component[] GetGameObjectComponentsInChildren(GameObject gameObject, Type type)" in content
    assert "internal static Component[] GetGameObjectComponentsInChildren(GameObject gameObject, Type type, bool includeInactive)" in content
    assert "internal static bool TryGetGameObjectComponentInChildren(GameObject gameObject, Type type, out Component? component)" in content
    assert "internal static bool TryGetGameObjectComponentInChildren(GameObject gameObject, Type type, bool includeInactive, out Component? component)" in content
    assert "internal static void GetGameObjectComponentsInChildren(GameObject gameObject, Type type, List<Component> results)" in content
    assert "internal static void GetGameObjectComponentsInChildren(GameObject gameObject, Type type, bool includeInactive, List<Component> results)" in content
    assert "internal static T[] GetGameObjectComponentsInParent<T>(GameObject gameObject) where T : Component" in content
    assert "internal static T[] GetGameObjectComponentsInParent<T>(GameObject gameObject, bool includeInactive) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponentInParent<T>(GameObject gameObject, out T? component) where T : Component" in content
    assert "internal static bool TryGetGameObjectComponentInParent<T>(GameObject gameObject, bool includeInactive, out T? component) where T : Component" in content
    assert "internal static void GetGameObjectComponentsInParent<T>(GameObject gameObject, List<T> results) where T : Component" in content
    assert "internal static void GetGameObjectComponentsInParent<T>(GameObject gameObject, bool includeInactive, List<T> results) where T : Component" in content
    assert "internal static Component[] GetGameObjectComponentsInParent(GameObject gameObject, Type type)" in content
    assert "internal static Component[] GetGameObjectComponentsInParent(GameObject gameObject, Type type, bool includeInactive)" in content
    assert "internal static bool TryGetGameObjectComponentInParent(GameObject gameObject, Type type, out Component? component)" in content
    assert "internal static bool TryGetGameObjectComponentInParent(GameObject gameObject, Type type, bool includeInactive, out Component? component)" in content
    assert "internal static void GetGameObjectComponentsInParent(GameObject gameObject, Type type, List<Component> results)" in content
    assert "internal static void GetGameObjectComponentsInParent(GameObject gameObject, Type type, bool includeInactive, List<Component> results)" in content
    assert "return GetGameObjectComponent(gameObject, typeof(T)) as T;" in content
    assert "return GetGameObjectComponentInChildren(gameObject, typeof(T), includeInactive) as T;" in content
    assert "return GetGameObjectComponentInParent(gameObject, typeof(T), includeInactive) as T;" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponent(this, out component);" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponent(this, type, out component);" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponentInChildren(this, includeInactive, out component);" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponentInChildren(this, type, includeInactive, out component);" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponentInParent(this, includeInactive, out component);" in content
    assert "return Managed.ManagedComponentBridge.TryGetGameObjectComponentInParent(this, type, includeInactive, out component);" in content
    assert "private static bool CanMatchManagedComponentType(Type type)" in content
    assert "if (expectedType.IsInstanceOfType(candidate))" in content
    assert "private static void CollectComponentsOnGameObject(GameObject gameObject, Type expectedType, List<Component> results)" in content
    assert "private static void CollectComponentsInChildren(GameObject gameObject, Type expectedType, bool includeInactive, bool includeSelf, List<Component> results)" in content
    assert "private static void CollectComponentsInParent(GameObject gameObject, Type expectedType, bool includeInactive, bool includeSelf, List<Component> results)" in content
    assert "public static Vector3 zero => new(0f, 0f, 0f);" in content
    assert "public static Vector3 right => new(1f, 0f, 0f);" in content
    assert "public static Vector3 up => new(0f, 1f, 0f);" in content
    assert "public static Vector3 forward => new(0f, 0f, 1f);" in content
    assert "public static Vector2 zero => new(0f, 0f);" in content
    assert "public static Vector2 one => new(1f, 1f);" in content
    assert "public float sqrMagnitude => X * X + Y * Y;" in content
    assert "public static Vector2 Lerp(Vector2 a, Vector2 b, float t)" in content
    assert "public float sqrMagnitude => X * X + Y * Y + Z * Z;" in content
    assert "public Vector3 normalized" in content
    assert "public static float Dot(Vector3 lhs, Vector3 rhs)" in content
    assert "public static Vector3 Cross(Vector3 lhs, Vector3 rhs)" in content
    assert "public static Quaternion Euler(Vector3 euler)" in content
    assert "public static Quaternion Euler(float x, float y, float z)" in content
    assert "public static Quaternion AngleAxis(float angle, Vector3 axis)" in content
    assert "public static Quaternion LookRotation(Vector3 forward)" in content
    assert "public static Quaternion LookRotation(Vector3 forward, Vector3 upwards)" in content
    assert "public static Quaternion operator *(Quaternion lhs, Quaternion rhs)" in content
    assert "public static Color white => new(1f, 1f, 1f, 1f);" in content
    assert "public float grayscale => 0.299f * r + 0.587f * g + 0.114f * b;" in content
    assert "public static Color Lerp(Color a, Color b, float t)" in content
    assert "public static implicit operator Color(Color32 value)" in content
    assert "public static Matrix4x4 identity => new(" in content
    assert "public Matrix4x4 inverse" in content
    assert "public static Matrix4x4 TRS(Vector3 position, Quaternion rotation, Vector3 scale)" in content
    assert "public Vector3 MultiplyPoint(Vector3 point)" in content
    assert "public Vector3 MultiplyVector(Vector3 vector)" in content
    assert "public static Matrix4x4 operator *(Matrix4x4 lhs, Matrix4x4 rhs)" in content
    assert "public Ray(Vector3 origin, Vector3 direction)" in content
    assert "public Vector3 GetPoint(float distance)" in content
    assert "public const float PI = MathF.PI;" in content
    assert "public static float Clamp01(float value)" in content
    assert "public static float Lerp(float a, float b, float t)" in content
    assert "public static float DeltaAngle(float current, float target)" in content
    assert "public static bool Approximately(float a, float b)" in content
    assert "public static float value => (float)_random.NextDouble();" in content
    assert "public static void InitState(int seed)" in content
    assert "public static int Range(int minInclusive, int maxExclusive)" in content
    assert "public static float Range(float minInclusive, float maxInclusive)" in content
    assert "public static bool GetTransformHasChanged(long gameObjectId)" in content
    assert "public static void SetTransformHasChanged(long gameObjectId, bool hasChanged)" in content
    assert "public static bool GetComponentEnabled(long componentId)" in content
    assert "public static long AddCameraComponent(long gameObjectId)" in content
    assert "public static long GetCameraComponentId(long gameObjectId)" in content
    assert "public static long GetMainCameraGameObjectId()" in content
    assert "public static CameraProjection GetCameraProjectionMode(long componentId)" in content
    assert "public static Vector3 CameraScreenToWorldPoint(long componentId, Vector3 position)" in content
    assert "public static Ray CameraScreenPointToRay(long componentId, Vector2 position)" in content
    assert "private static readonly Dictionary<long, Camera> NativeCameras = new();" in content
    assert "Camera camera => (T?)(Object?)InstantiateCamera(camera, parent)," in content
    assert "if (type == typeof(Camera))" in content
    assert "Camera? camera = GetNativeCameraOnGameObject(gameObject);" in content
    assert "internal static Camera? GetMainCamera()" in content

