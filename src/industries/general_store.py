"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryTertiary, TileLocationChecks, IndustryLocationChecks

industry = IndustryTertiary(id='general_store',
                    accept_cargo_types=['FOOD', 'GOOD', 'BEER'],
                    prod_cargo_types=[],
                    layouts='AUTO',
                    prob_in_game='12',
                    prob_random='24',
                    prod_multiplier='[0, 0]',
                    map_colour='14',
                    life_type='IND_LIFE_TYPE_BLACK_HOLE',
                    spec_flags='bitmask(IND_FLAG_ONLY_IN_TOWNS)',
                    location_checks=IndustryLocationChecks(incompatible={'general_store': 20,
                                                                         'petrol_pump': 16,
                                                                         'hotel': 16}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_GENERAL_STORE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_TOWN))',
                    fund_cost_multiplier='15' )

industry.economy_variations['BASIC_TEMPERATE'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_TROPIC'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].enabled = True
industry.economy_variations['MISTAH_KURTZ'].prob_random = '14'
industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='general_store_tile_1',
                  location_checks=TileLocationChecks(road_adjacent=['nw', 'ne', 'sw', 'se']))

spriteset_ground = industry.add_spriteset(
    id = 'general_store_spriteset_ground',
    type='slab',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'general_store_spriteset_ground_overlay',
    sprites = [(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(
    id = 'general_store_spriteset',
    sprites = [(10, 60, 64, 48, -31, -18)]
)
industry.add_spritelayout(
    id = 'general_store_spritelayout',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1]
)
industry.add_industry_layout(
    id = 'general_store_industry_layout',
    layout = [(0, 0, 'general_store_tile_1', 'general_store_spritelayout')]
)
