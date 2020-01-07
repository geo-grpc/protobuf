extern crate protoc_grpcio;

fn main() {
    if !std::env::var("REBUILD").and(Ok(true)).unwrap_or_default() {
        return;
    }

    let proto_lib_root = "src/proto";
    let proto_root = "../proto";
    let proto_files = [
        "epl/protobuf/geometry.proto",
        "epl/protobuf/query.proto",
        "epl/protobuf/stac.proto",
        "epl/protobuf/geometry_service.proto",
        "epl/protobuf/stac_service.proto",
    ];

    println!("cargo:rerun-if-changed={}", proto_root);
    protoc_grpcio::compile_grpc_protos(
        &proto_files,
        &[proto_root],
        &proto_lib_root,
        Some(protobuf_codegen::Customize {
            serde_derive: Some(true),
            ..Default::default()
        }),
    )
    .expect("Failed to compile gRPC definitions!");
}
