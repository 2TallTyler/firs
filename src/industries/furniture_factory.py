"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='furniture_factory',
                    processed_cargos_and_output_ratios=[('MNSP', 3), ('WDPR', 5)],
                    combined_cargos_boost_prod=True,
                    prod_cargo_types=['GOOD'],
                    layouts='AUTO',
                    prob_in_game='7',
                    prob_random='8',
                    prod_multiplier='[0, 0]',
                    map_colour='186',
                    location_checks=IndustryLocationChecks(incompatible={'furniture_factory': 56}),
                    remove_cost_multiplier='0',
                    name='string(STR_IND_FURNITURE_FACTORY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='95')

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True

industry.add_tile(id='furniture_factory_tile_1',
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))


spriteset_ground = industry.add_spriteset(
    id = 'furniture_factory_spriteset_ground',
    type='cobble',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'furniture_factory_spriteset_ground_overlay',
    type='empty',
)
spriteset_1 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_1',
    sprites = [(10, 60, 64, 88, -31, -42)],
)
spriteset_2 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_2',
    sprites = [(80, 60, 64, 88, -31, -44)],
)
spriteset_3 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_3',
    sprites = [(150, 60, 64, 88, -31, -42)],
)
spriteset_4 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_4',
    sprites = [(220, 60, 64, 88, -31, -42)],
)
spriteset_5 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_5',
    sprites = [(290, 60, 64, 88, -31, -42)],
)
spriteset_6 = industry.add_spriteset(
    id = 'furniture_factory_spriteset_6',
    sprites = [(360, 60, 64, 88, -31, -41)],
)

industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'furniture_factory_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'furniture_factory_industry_layout_1',
    layout = [(0, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (1, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_5'),
              (1, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (2, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_4'),
              (2, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'furniture_factory_industry_layout_2',
    layout = [(0, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_5'),
              (0, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (1, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_4'),
              (1, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (2, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
              (2, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'furniture_factory_industry_layout_3',
    layout = [(0, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (0, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
              (1, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (1, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (2, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
              (2, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (3, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_5'),
              (3, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
              (4, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_4'),
              (4, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
    ]
)
industry.add_industry_layout(
    id = 'furniture_factory_industry_layout_4',
    layout = [(0, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_5'),
              (0, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
              (1, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_4'),
              (1, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
              (2, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (2, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (3, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (3, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (4, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
              (4, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
    ]
)
industry.add_industry_layout(
    id = 'furniture_factory_industry_layout_5',
    layout = [(0, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_5'),
              (0, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (0, 2, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_3'),
              (1, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_4'),
              (1, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (1, 2, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_2'),
              (2, 0, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_6'),
              (2, 1, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
              (2, 2, 'furniture_factory_tile_1', 'furniture_factory_spritelayout_1'),
    ]
)
