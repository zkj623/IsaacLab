# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for custom terrains."""

import omni.isaac.lab.terrains as terrain_gen
from omni.isaac.lab.terrains import FlatPatchSamplingCfg

from ..terrain_generator_cfg import TerrainGeneratorCfg

ROUGH_TERRAINS_CFG = TerrainGeneratorCfg(
    size=(8.0, 8.0),
    border_width=20.0,
    num_rows=10,
    num_cols=20,
    horizontal_scale=0.1,
    vertical_scale=0.005,
    slope_threshold=0.75,
    use_cache=False,
    sub_terrains={
        "pyramid_stairs": terrain_gen.MeshPyramidStairsTerrainCfg(
            proportion=0.,
            step_height_range=(0.05, 0.18),
            step_width=0.3,
            platform_width=3.0,
            border_width=1.0,
            holes=False,
            flat_patch_sampling={
                "target": FlatPatchSamplingCfg(num_patches=30, patch_radius=0.3, max_height_diff=0.05)
            }
        ),
        "pyramid_stairs_inv": terrain_gen.MeshInvertedPyramidStairsTerrainCfg(
            proportion=0.,
            step_height_range=(0.05, 0.18),
            step_width=0.3,
            platform_width=3.0,
            border_width=1.0,
            holes=False,
            flat_patch_sampling={
                "target": FlatPatchSamplingCfg(num_patches=30, patch_radius=0.3, max_height_diff=0.05)
            }
        ),
        "boxes": terrain_gen.MeshRandomGridTerrainCfg(
            proportion=0.1, grid_width=0.45, grid_height_range=(0.05, 0.2), platform_width=2.0,
            flat_patch_sampling={
                "target": FlatPatchSamplingCfg(num_patches=30, patch_radius=0.3, max_height_diff=0.05)
            }

        ),
        "random_rough": terrain_gen.HfRandomUniformTerrainCfg(
            proportion=0.1, noise_range=(0.02, 0.10), noise_step=0.02, border_width=0.25,
            flat_patch_sampling={
                "target": FlatPatchSamplingCfg(num_patches=30, patch_radius=0.3, max_height_diff=0.05)
            }
        ),
        "hf_pyramid_slope": terrain_gen.HfPyramidSlopedTerrainCfg(
            proportion=0., slope_range=(0.0, 0.4), platform_width=2.0, border_width=0.25
        ),
        "hf_pyramid_slope_inv": terrain_gen.HfInvertedPyramidSlopedTerrainCfg(
            proportion=0., slope_range=(0.0, 0.4), platform_width=2.0, border_width=0.25
        ),
        "rails": terrain_gen.MeshRailsTerrainCfg(
            proportion=0., rail_thickness_range=(0.2,0.2), rail_height_range=(0.2,0.2), platform_width=2.0
        ),
        "pit": terrain_gen.MeshPitTerrainCfg(
            proportion=0.8, pit_depth_range=(0.15,0.3), platform_width=3.0,
            flat_patch_sampling={
                "target": FlatPatchSamplingCfg(num_patches=30, patch_radius=0.3, max_height_diff=0.05)
            }
        ),
        "gap": terrain_gen.MeshGapTerrainCfg(
            proportion=0., gap_width_range=(0.15,0.3), platform_width=3.0
        ),
    },
)
"""Rough terrains configuration."""
