import Release.lidar_odometry_py as lo
import Release.multi_view_tls_registration_py as mvr
from pathlib import Path

DATA_DIR = Path(
    R"C:\Users\Admin\Documents\Mosaic\hdmapping_experiments\lidar_1_automatic"
)

lo_params = lo.LidarOdometryParams()
lo_params.in_out_params.resolution_X = 0.3
lo_params.in_out_params.resolution_Y = 0.3
lo_params.in_out_params.resolution_Z = 0.3

lo.run_lidar_odometry(
    str(DATA_DIR),
    lo_params,
    output_las_name=str(DATA_DIR / "all.laz"),
    trajectory_ascii_name=str(DATA_DIR / "traj_lo.csv"),
)

mvr_params = mvr.TLSRegistration()
mvr_params.initial_pose_to_identity = True
mvr_params.use_pgslam = True
mvr_params.output_las_name = str(DATA_DIR / "all_mvr_pgslam.laz")
mvr_params.trajectories_name = str(DATA_DIR / "traj_mvr_pgslam.csv")
mvr.run_multi_view_tls_registration(
    str(DATA_DIR / "session.json"),
    str(DATA_DIR / "session_mvr_pgslam.json"),
    mvr_params,
)