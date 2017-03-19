"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""

from industry import IndustrySecondary, TileLocationChecks, IndustryLocationChecks

industry = IndustrySecondary(id='sugar_refinery',
                    processed_cargos_and_output_ratios=[('MNSP', 3), ('SGBT', 5)],
                    combined_cargos_boost_prod=True,
                    prod_cargo_types=['FOOD'],
                    layouts='AUTO',
                    prob_in_game='3',
                    prob_random='5',
                    prod_multiplier='[0, 0]',
                    map_colour='83',
                    spec_flags='bitmask(IND_FLAG_MILITARY_AIRPLANE_CAN_EXPLODE)',
                    location_checks=IndustryLocationChecks(incompatible={'sugar_refinery': 56,
                                                                         'arable_farm': 16}),
                    remove_cost_multiplier='0',
                    name='string(STR_IND_SUGAR_REFINERY)',
                    nearby_station_name='string(STR_STATION, string(STR_TOWN), string(STR_STATION_REFINERY))',
                    fund_cost_multiplier='140')

industry.economy_variations['FIRS'].enabled = True

industry.add_tile(id='sugar_refinery_tile_1',
                  animation_length=7,
                  animation_looping=True,
                  animation_speed=3,
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

spriteset_ground = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_ground',
    type = 'concrete'
)
spriteset_ground_overlay = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_ground_overlay',
    type = 'empty'
)
spriteset_1 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_1',
    sprites = [(10, 10, 64, 50, -31, -23)],
)
spriteset_2 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_2',
    sprites = [(80, 10, 64, 50, -31, -25)],
)
spriteset_3 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_3',
    sprites = [(150, 10, 64, 88, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_4',
    sprites = [(220, 10, 64, 88, -31, -58)],
)
spriteset_5 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_5',
    sprites = [(290, 10, 64, 88, -31, -58)],
)
spriteset_6 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_6',
    sprites = [(360, 10, 64, 88, -31, -58)],
)
spriteset_7 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_7',
    sprites = [(430, 10, 64, 88, -31, -58)],
)
spriteset_8 = industry.add_spriteset(
    id = 'sugar_refinery_spriteset_8',
    sprites = [(500, 10, 64, 88, -31, -58)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 5,
    yoffset= 8,
    zoffset= 72,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type = 'white_smoke_big',
    xoffset= 5,
    yoffset= 12,
    zoffset= 72,
    animation_frame_offset = 1
)

industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_1',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_1],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_2',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_3',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_3],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_4',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_4],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_5',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_5],
    fences = ['se']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_6',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_6],
    smoke_sprites = [sprite_smoke_1, sprite_smoke_2],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_7',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_7],
    fences = []
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_8',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [spriteset_8],
    fences = ['nw','ne','se','sw']
)
industry.add_spritelayout(
    id = 'sugar_refinery_spritelayout_9',
    ground_sprite = spriteset_ground,
    ground_overlay = spriteset_ground_overlay,
    building_sprites = [],
    fences = ['nw','ne','se','sw']
)

industry.add_industry_layout(
    id = 'sugar_refinery_industry_layout_1',
    layout = [(0, 0, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_4'),
              (0, 1, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_4'),
              (0, 2, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_4'),
              (1, 0, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_8'),
              (1, 1, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_3'),
              (1, 2, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_1'),
              (2, 0, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_6'),
              (2, 1, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_9'),
              (2, 2, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_2'),
              (3, 0, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_7'),
              (3, 1, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_7'),
              (3, 2, 'sugar_refinery_tile_1', 'sugar_refinery_spritelayout_5')
    ]
)

