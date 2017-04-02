"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustryPrimaryExtractive, TileLocationChecks

industry = IndustryPrimaryExtractive(id='dredging_site',
                    prod_cargo_types=['SAND', 'GRVL'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[17, 17]',
                    map_colour='195',
                    spec_flags='bitmask(IND_FLAG_BUILT_ON_WATER, IND_FLAG_AI_CREATES_AIR_AND_SHIP_ROUTES)',
                    location_checks=dict(coast_distance=True),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_DREDGING_SITE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_WATER))',
                    fund_cost_multiplier='180',
                    graphics_change_dates = [1906, 1945])

industry.economy_variations['FIRS'].enabled = True
industry.economy_variations['BASIC_TEMPERATE'].enabled = True

industry.add_tile(id='dredging_site_tile_1',
                  location_checks=TileLocationChecks(disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDSPRITE_WATER',
)

spriteset_ground_overlay = industry.add_spriteset(
    id = 'dredging_site_spriteset_ground_overlay',
    type='empty',
)

spriteset_platform = industry.add_spriteset(
    id = 'dredging_site_spriteset_platform',
    sprites = [(10, 10, 64, 100, -31, -65)],
)
spriteset_greeble = industry.add_spriteset(
    id = 'dredging_site_spriteset_greeble',
    sprites = [(80, 10, 64, 39, -31, -10)],
)
spriteset_crane_animated = industry.add_spriteset(
    id = 'dredging_site_spriteset_spriteset_crane_animated',
    sprites = [(150, 10, 64, 64, -33, -35)],
)

industry.add_spritelayout(
    id = 'dredging_site_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_platform,
    building_sprites = [spriteset_crane_animated, spriteset_greeble]
)
industry.add_spritelayout(
    id = 'dredging_site_spritelayout_null',
    ground_sprite = sprite_ground,
    ground_overlay = sprite_ground,
    building_sprites = []
)

industry.add_industry_layout(
    id = 'dredging_site_industry_layout_1',
    layout = [(0, 0, '255', 'dredging_site_spritelayout_null'),
              (0, 1, '24', 'dredging_site_spritelayout_null'),
              (0, 2, '24', 'dredging_site_spritelayout_null'),
              (0, 4, '255', 'dredging_site_spritelayout_null'),
              (1, 0, '255', 'dredging_site_spritelayout_null'),
              (1, 4, '255', 'dredging_site_spritelayout_null'),
              (2, 0, '255', 'dredging_site_spritelayout_null'),
              (2, 2, '255', 'dredging_site_spritelayout_null'),
              (2, 3, 'dredging_site_tile_1', 'dredging_site_spritelayout_1'),
              (2, 4, '255', 'dredging_site_spritelayout_null'),
    ]
)
