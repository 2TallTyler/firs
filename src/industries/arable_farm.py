"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryOrganic, TileLocationChecks

industry = IndustryPrimaryOrganic(id='arable_farm',
                    prod_cargo_types=['GRAI', 'SGBT'],
                    layouts='AUTO',
                    prob_in_game='4',
                    prob_random='11',
                    prod_multiplier='[14, 14]',
                    map_colour='208',
                    spec_flags='bitmask(IND_FLAG_PLANT_FIELDS_PERIODICALLY, IND_FLAG_PLANT_FIELDS_WHEN_BUILT)',
                    location_checks=dict(require_cluster=['arable_farm', [20, 72, 1, 4]]),
                    prospect_chance='0.75',
                    name='string(STR_IND_ARABLE_FARM)',
                    extra_text_fund='string(STR_FUND_ARABLE_FARM)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_FARM))',
                    fund_cost_multiplier='55',
                    graphics_change_dates = [1928] )

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].prod_cargo_types = ['GRAI', 'BEAN']
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prod_cargo_types = ['CASS', 'NUTS']

industry.add_tile(id='arable_farm_tile_1',
                  location_checks=TileLocationChecks(disallow_slopes=True,
                                                     disallow_above_snowline=True,
                                                     disallow_desert=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS'
)
spriteset_ground_empty = industry.add_spriteset(
    id = 'arable_farm_spriteset_ground',
    type = 'empty'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'arable_farm_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'arable_farm_spriteset_1',
    sprites = [(10, 10, 64, 59, -31, -28)],
)
spriteset_2 = industry.add_spriteset(
    id = 'arable_farm_spriteset_2',
    sprites = [(80, 10, 64, 59, -31, -28)],
)
spriteset_3 = industry.add_spriteset(
    id = 'arable_farm_spriteset_3',
    sprites = [(150, 10, 64, 59, -31, -28)],
)
spriteset_4 = industry.add_spriteset(
    id = 'arable_farm_spriteset_4',
    sprites = [(220, 10, 64, 59, -31, -28)],
)
spriteset_5 = industry.add_spriteset(
    id = 'arable_farm_spriteset_5',
    sprites = [(290, 10, 64, 59, -31, -28)],
)

industry.add_spritelayout(
    id = 'arable_farm_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_spritelayout(
    id = 'arable_farm_spritelayout_2',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'arable_farm_spritelayout_3',
    ground_sprite = spriteset_ground_empty,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    terrain_aware_ground = True
)
industry.add_spritelayout(
    id = 'arable_farm_spritelayout_4',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
)
industry.add_spritelayout(
    id = 'arable_farm_spritelayout_5',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
)

industry.add_industry_layout(
    id = 'arable_farm_industry_layout_1',
    layout = [(0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
              (0, 2, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
              (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
              (1, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
              (2, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
    ]
)
industry.add_industry_layout(
    id = 'arable_farm_industry_layout_2',
    layout = [(0, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
              (0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
              (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
              (1, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
              (2, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
    ]
)
industry.add_industry_layout(
    id = 'arable_farm_industry_layout_3',
    layout = [(0, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_1'),
              (0, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_2'),
              (1, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_5'),
              (2, 0, 'arable_farm_tile_1', 'arable_farm_spritelayout_4'),
              (2, 1, 'arable_farm_tile_1', 'arable_farm_spritelayout_3'),
    ]
)
