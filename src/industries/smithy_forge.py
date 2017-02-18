"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='smithy_forge',
                    processed_cargos_and_output_ratios=[('METL', 8)],
                    prod_increase_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_INCREASE_GENERAL',
                    prod_cargo_types=['ENSP', 'FMSP'],
                    layouts='AUTO',
                    prob_in_game='2',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    substitute='0',
                    new_ind_msg='TTD_STR_NEWS_INDUSTRY_CONSTRUCTION',
                    map_colour='133',
                    prod_decrease_msg='TTD_STR_NEWS_INDUSTRY_PRODUCTION_DECREASE_GENERAL',
                    min_cargo_distr='5',
                    spec_flags='bitmask(IND_FLAG_ONLY_IN_TOWNS)',
                    location_checks=IndustryLocationChecks(incompatible={'smithy_forge': 56}),
                    remove_cost_multiplier='0',
                    prospect_chance='0.75',
                    name='string(STR_IND_SMITHY_FORGE)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_INDUSTRY_ESTATE))',
                    fund_cost_multiplier='63',
                    closure_msg='TTD_STR_NEWS_INDUSTRY_CLOSURE_SUPPLY_PROBLEMS',
                    expiry_year=1948 )

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='smithy_forge_tile_1',
                  animation_length=47,
                  animation_looping=True,
                  animation_speed=2,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number = 'GROUNDTILE_MUD_TRACKS',
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'smithy_forge_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'smithy_forge_spriteset_1',
    sprites = [(10, 10, 64, 80, -31, -49)],
    zextent = 48
)
spriteset_2 = industry.add_spriteset(
    id = 'smithy_forge_spriteset_2',
    sprites = [(80, 10, 64, 80, -31, -49)],
    zextent = 48
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type = 'dark_smoke_small',
    xoffset= 0,
    yoffset= 1,
    zoffset= 44,
)

industry.add_spritelayout(
    id = 'smithy_forge_spritelayout_1',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    smoke_sprites = [sprite_smoke],
    fences = ['se','sw']
)
industry.add_spritelayout(
    id = 'smithy_forge_spritelayout_2',
    ground_sprite = sprite_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['se','sw']
)
industry.add_industry_layout(
    id = 'smithy_forge_industry_layout',
    layout = [(0, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_2'),
              (1, 0, 'smithy_forge_tile_1', 'smithy_forge_spritelayout_1'),
    ]
)

