"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='pipe_mill',
                    processed_cargos_and_output_ratios=[('STEL', 8)],
                    combined_cargos_boost_prod=True,
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['PIPE'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='38',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='0',
                    location_checks=IndustryLocationChecks(incompatible={'pipe_mill': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_PIPE_MILL)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_HEAVY_INDUSTRY))',
                    fund_cost_multiplier='110',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    intro_year=1832 )

# not currently in use
#industry.economy_variations['STEELTOWN'].enabled = True


industry.add_tile(id='pipe_mill_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    id = 'pipe_mill_spriteset_ground',
    type = 'concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'pipe_mill_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_1',
    sprites = [(10, 60, 64, 70, -31, -35)],
    zextent = 32
)
spriteset_2 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_2',
    sprites = [(80, 60, 64, 70, -31, -35)],
    zextent = 32
)
spriteset_3 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_3',
    sprites = [(150, 60, 64, 51, -31, -20)],
    zextent = 32
)
spriteset_4 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_4',
    sprites = [(220, 60, 64, 51, -31, -23)],
    zextent = 32
)
spriteset_5 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_5',
    sprites = [(290, 60, 64, 51, -31, -20)],
    zextent = 32
)
spriteset_6 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_6',
    sprites = [(360, 60, 64, 31, -31, 0)],
    zextent = 32
)
spriteset_7 = industry.add_spriteset(
    id = 'pipe_mill_spriteset_7',
    sprites = [(430, 60, 64, 31, -31, 0)],
    zextent = 32
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_small',
    xoffset= -5,
    yoffset= 0,
    zoffset= 26,
)

industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    smoke_sprites = [sprite_smoke],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'pipe_mill_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'pipe_mill_industry_layout_1',
    layout = [(0, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_4'),
              (0, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
              (0, 4, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (1, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (1, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
              (1, 4, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (2, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (2, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_1'),
              (2, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_2'),
              (2, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (2, 4, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
    ]
)
industry.add_industry_layout(
    id = 'pipe_mill_industry_layout_2',
    layout = [(0, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_1'),
              (1, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_2'),
              (1, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (2, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (2, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (2, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
              (2, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
              (3, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_4'),
              (3, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (3, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (3, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
    ]
)
industry.add_industry_layout(
    id = 'pipe_mill_industry_layout_3',
    layout = [(0, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (0, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (1, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_3'),
              (1, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
              (2, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (2, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_1'),
              (2, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_2'),
              (2, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (3, 0, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_5'),
              (3, 1, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_4'),
              (3, 2, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_7'),
              (3, 3, 'pipe_mill_tile_1', 'pipe_mill_spritelayout_6'),
    ]
)
