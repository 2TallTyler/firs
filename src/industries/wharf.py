from industry import IndustryPrimaryPort, TileLocationChecks

industry = IndustryPrimaryPort(id='wharf',
                               accept_cargo_types=[],
                               prod_cargo_types_with_multipliers=[],
                               prob_in_game='2',
                               prob_map_gen='6',
                               map_colour='37',
                               special_flags=['IND_FLAG_BUILT_ON_WATER'],
                               location_checks=dict(same_type_distance=16),
                               prospect_chance='0.75',
                               name='string(STR_IND_WHARF)',
                               nearby_station_name='string(STR_STATION_INDUSTRY_HARBOUR_3)',
                               fund_cost_multiplier='152',
                               override_default_construction_states=True)

industry.economy_variations['BASIC_ARCTIC'].enabled = True
industry.economy_variations['BASIC_ARCTIC'].accept_cargo_types = ['BOOM', 'PEAT', 'WDPR']
industry.economy_variations['BASIC_ARCTIC'].prod_cargo_types_with_multipliers = [('POTA', 19), ('ENSP', 9), ('FMSP', 9)]

# in Steeltown, there is a deliberate feedback loop with ZINC -> PIPE -> wharf
# this is to allow an easy kickstart of ENSP at the wharf, when all other chains are so tightly connected
industry.economy_variations['STEELTOWN'].enabled = True
industry.economy_variations['STEELTOWN'].accept_cargo_types = ['CMNT', 'PIPE', 'RBAR', 'MNSP'] # FOOD was tried, but results in more complex cargo flow diagram
industry.economy_variations['STEELTOWN'].prod_cargo_types_with_multipliers = [('ENSP', 12), ('POWR', 14), ('ZINC', 16), ('COAT', 10), ('ALUM', 11), ('SOAP', 10)]

"""
industry.economy_variations['IN_A_HOT_COUNTRY'].enabled = True
industry.economy_variations['IN_A_HOT_COUNTRY'].accept_cargo_types = ['COPR']
industry.economy_variations['IN_A_HOT_COUNTRY'].prod_cargo_types_with_multipliers = [('QLME', 14), ('POTA', 16), ('VEHI', 16)]
"""

industry.add_tile(id='wharf_tile_1',
                  land_shape_flags='bitmask(LSF_ONLY_ON_FLAT_LAND)',
                  location_checks=TileLocationChecks(always_allow_founder=False))
industry.add_tile(id='wharf_tile_2',
                  foundations='return CB_RESULT_NO_FOUNDATIONS',
                  location_checks=TileLocationChecks(always_allow_founder=False,
                                                     require_coast=True))

# empty tile
# covered store
# tanks
# silos
# cone silo
# warehouse
# large crane (4 angles)
# boat 1
# boat 2

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDSPRITE_WATER'
)
spriteset_ground_empty = industry.add_spriteset(
    type='empty'
)
spriteset_concrete = industry.add_spriteset(
    sprites=[(10, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_crane_rails_nw_se = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_crane_rails_ne_sw = industry.add_spriteset(
    sprites=[(150, 10, 64, 39, -31, -8)],
    always_draw=1,
)
spriteset_jetty_se_nw = industry.add_spriteset(
    sprites=[(10, 60, 64, 39, -31, -7)],
    always_draw=1,
)
spriteset_jetty_ne_sw = industry.add_spriteset(
    sprites=[(80, 60, 64, 39, -31, -7)],
    always_draw=1
)
spriteset_jetty_slope_nw_se = industry.add_spriteset(
    sprites=[(150, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_ne_sw = industry.add_spriteset(
    sprites=[(220, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_se_nw = industry.add_spriteset(
    sprites=[(290, 60, 64, 39, -31, -7)],
)
spriteset_jetty_slope_sw_ne = industry.add_spriteset(
    sprites=[(360, 60, 64, 39, -31, -7)],
)
spriteset_tanks = industry.add_spriteset(
    sprites=[(440, 10, 64, 84, -31, -43)],
    zoffset=18
)
spriteset_silos = industry.add_spriteset(
    sprites=[(510, 10, 64, 84, -35, -61)],
)
spriteset_cone_silo = industry.add_spriteset(
    sprites=[(580, 10, 64, 84, -31, -61)],
)
spriteset_warehouse = industry.add_spriteset(
    sprites=[(650, 10, 64, 84, -31, -61)],
)
spriteset_large_crane_ne_sw = industry.add_spriteset(
    sprites=[(440, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_nw_se = industry.add_spriteset(
    sprites=[(510, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_se_nw = industry.add_spriteset(
    sprites=[(580, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_large_crane_sw_ne = industry.add_spriteset(
    sprites=[(650, 110, 64, 84, -31, -43)],
    zoffset=18,
)
spriteset_boat_1 = industry.add_spriteset(
    sprites=[(10, 110, 64, 39, -35, -15)],
)
spriteset_boat_2 = industry.add_spriteset(
    sprites=[(80, 110, 64, 39, -40, -12)],
)
spriteset_boat_3 = industry.add_spriteset(
    sprites=[(150, 110, 64, 39, -13, -19)],
)
spriteset_boat_4 = industry.add_spriteset(
    sprites=[(220, 110, 64, 39, -27, -12)],
)
spriteset_boat_5 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -15, -11)],
)
spriteset_boat_6 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -25, -20)],
)
spriteset_boat_7 = industry.add_spriteset(
    sprites=[(360, 110, 64, 39, -29, -5)],
)
spriteset_boat_8 = industry.add_spriteset(
    sprites=[(290, 110, 64, 39, -32, -21)],
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_rails_nw_se',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_crane_rails_nw_se]
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_rails_ne_sw',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_crane_rails_ne_sw]
)
industry.add_spritelayout(
    id='wharf_spritelayout_11',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_concrete, spriteset_silos]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_barge_sw_ne',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_1]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_barge_ne_sw',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_2]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_barge_se_nw',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_3]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_barge_nw_se',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_4]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_empty',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_coaster_ne_sw',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_5]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_coaster_nw_se',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_6]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_coaster_se_nw',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_7]
)
industry.add_spritelayout(
    id='wharf_spritelayout_water_coaster_sw_ne',
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_boat_8]
)
industry.add_spritelayout(
    id='wharf_spritelayout_cone_silo',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_cone_silo]
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_nw_se',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_nw_se]
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_sw_ne',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_sw_ne]
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_ne_sw',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_ne_sw]
)
industry.add_spritelayout(
    id='wharf_spritelayout_crane_se_nw',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete, spriteset_large_crane_se_nw]
)
industry.add_spritelayout(
    id='wharf_spritelayout_jetty_empty',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[spriteset_jetty_se_nw, spriteset_jetty_ne_sw, spriteset_concrete]
)
industry.add_spritelayout(
    id='wharf_spritelayout_null',
    ground_sprite=spriteset_ground_empty,
    ground_overlay=spriteset_ground_empty,
    building_sprites=[]
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='wharf_spritelayout_coast_tanks',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_tanks],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)
industry.add_magic_spritelayout(
    type='harbour_coast_foundations',
    base_id='wharf_spritelayout_coast_warehouse',
    config={'ground_sprite': spriteset_ground_empty,  # should alqways be empty for this magic spritelayout
            'building_sprites': [spriteset_concrete, spriteset_warehouse],
            'foundation_sprites': {'ne_sw': spriteset_jetty_ne_sw,
                                   'se_nw': spriteset_jetty_se_nw,
                                   'slope_nw_se': spriteset_jetty_slope_nw_se,
                                   'slope_ne_sw': spriteset_jetty_slope_ne_sw,
                                   'slope_se_nw': spriteset_jetty_slope_se_nw,
                                   'slope_sw_ne': spriteset_jetty_slope_sw_ne}}
)

industry.add_industry_layout(
    id='wharf_industry_layout_1',
    layout=[
        (0, 0, '255', 'wharf_spritelayout_null'),
        (0, 1, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (0, 2, 'wharf_tile_1', 'wharf_spritelayout_water_coaster_se_nw'),
        (0, 3, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (0, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_se_nw'),
        (0, 5, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
        (1, 0, '255', 'wharf_spritelayout_null'),
        (1, 1, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
        (1, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_se_nw'),
        (1, 3, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
        (1, 4, 'wharf_tile_1', 'wharf_spritelayout_jetty_empty'),
        (1, 5, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
        (2, 0, '255', 'wharf_spritelayout_null'),
        (2, 1, 'wharf_tile_1', 'wharf_spritelayout_water_barge_se_nw'),
        (2, 2, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (2, 3, 'wharf_tile_1', 'wharf_spritelayout_water_barge_se_nw'),
        (2, 4, 'wharf_tile_1', 'wharf_spritelayout_cone_silo'),
        (2, 5, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
        (3, 0, '255', 'wharf_spritelayout_null'),
        (3, 1, 'wharf_tile_1', 'wharf_spritelayout_crane_se_nw'),
        (3, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_se_nw'),
        (3, 3, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
        (3, 4, 'wharf_tile_1', 'wharf_spritelayout_11'),
        (3, 5, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
        (4, 0, '255', 'wharf_spritelayout_null'),
        (4, 1, '255', 'wharf_spritelayout_null'),
        (4, 2, '255', 'wharf_spritelayout_null'),
        (4, 3, '255', 'wharf_spritelayout_null'),
        (4, 4, '255', 'wharf_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_2',
    layout=[(0, 0, '255', 'wharf_spritelayout_null'),
            (0, 1, '255', 'wharf_spritelayout_null'),
            (0, 2, '255', 'wharf_spritelayout_null'),
            (0, 3, '255', 'wharf_spritelayout_null'),
            (0, 4, '255', 'wharf_spritelayout_null'),
            (1, 0, 'wharf_tile_1', 'wharf_spritelayout_crane_ne_sw'),
            (1, 1, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (1, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
            (1, 3, 'wharf_tile_1', 'wharf_spritelayout_water_barge_sw_ne'),
            (1, 4, '255', 'wharf_spritelayout_null'),
            (2, 0, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_water_coaster_sw_ne'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_ne_sw'),
            (2, 3, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (2, 4, '255', 'wharf_spritelayout_null'),
            (3, 0, 'wharf_tile_1', 'wharf_spritelayout_crane_ne_sw'),
            (3, 1, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (3, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
            (3, 3, 'wharf_tile_1', 'wharf_spritelayout_water_barge_sw_ne'),
            (3, 4, '255', 'wharf_spritelayout_null'),
            (4, 0, 'wharf_tile_1', 'wharf_spritelayout_11'),
            (4, 1, 'wharf_tile_1', 'wharf_spritelayout_cone_silo'),
            (4, 2, 'wharf_tile_1', 'wharf_spritelayout_jetty_empty'),
            (4, 3, 'wharf_tile_1', 'wharf_spritelayout_crane_ne_sw'),
            (4, 4, '255', 'wharf_spritelayout_null'),
            (5, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
            (5, 1, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
            (5, 2, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
            (5, 3, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
            ]

)
industry.add_industry_layout(
    id='wharf_industry_layout_3',
    layout=[
        (0, 1, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
        (0, 2, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
        (0, 3, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
        (0, 4, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
        (1, 0, '255', 'wharf_spritelayout_null'),
        (1, 1, 'wharf_tile_1', 'wharf_spritelayout_crane_sw_ne'),
        (1, 2, 'wharf_tile_1', 'wharf_spritelayout_jetty_empty'),
        (1, 3, 'wharf_tile_1', 'wharf_spritelayout_11'),
        (1, 4, 'wharf_tile_1', 'wharf_spritelayout_cone_silo'),
        (2, 0, '255', 'wharf_spritelayout_null'),
        (2, 1, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (2, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
        (2, 3, 'wharf_tile_1', 'wharf_spritelayout_water_barge_ne_sw'),
        (2, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_sw_ne'),
        (3, 0, '255', 'wharf_spritelayout_null'),
        (3, 1, 'wharf_tile_1', 'wharf_spritelayout_water_coaster_ne_sw'),
        (3, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_sw_ne'),
        (3, 3, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (3, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
        (4, 0, '255', 'wharf_spritelayout_null'),
        (4, 1, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
        (4, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_ne_sw'),
        (4, 3, 'wharf_tile_1', 'wharf_spritelayout_water_barge_ne_sw'),
        (4, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_sw_ne'),
        (5, 0, '255', 'wharf_spritelayout_null'),
        (5, 1, '255', 'wharf_spritelayout_null'),
        (5, 2, '255', 'wharf_spritelayout_null'),
        (5, 3, '255', 'wharf_spritelayout_null'),
        (5, 4, '255', 'wharf_spritelayout_null'),
    ]
)
industry.add_industry_layout(
    id='wharf_industry_layout_4',
    layout=[(0, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
            (0, 1, 'wharf_tile_1', 'wharf_spritelayout_11'),
            (0, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_nw_se'),
            (0, 3, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
            (0, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_nw_se'),
            (0, 5, '255', 'wharf_spritelayout_null'),
            (1, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_tanks'),
            (1, 1, 'wharf_tile_1', 'wharf_spritelayout_cone_silo'),
            (1, 2, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (1, 3, 'wharf_tile_1', 'wharf_spritelayout_water_coaster_nw_se'),
            (1, 4, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (1, 5, '255', 'wharf_spritelayout_null'),
            (2, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
            (2, 1, 'wharf_tile_1', 'wharf_spritelayout_jetty_empty'),
            (2, 2, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
            (2, 3, 'wharf_tile_1', 'wharf_spritelayout_crane_nw_se'),
            (2, 4, 'wharf_tile_1', 'wharf_spritelayout_crane_rails_nw_se'),
            (2, 5, '255', 'wharf_spritelayout_null'),
            (3, 0, 'wharf_tile_2', 'wharf_spritelayout_coast_warehouse'),
            (3, 1, 'wharf_tile_1', 'wharf_spritelayout_crane_nw_se'),
            (3, 2, 'wharf_tile_1', 'wharf_spritelayout_water_barge_nw_se'),
            (3, 3, 'wharf_tile_1', 'wharf_spritelayout_water_empty'),
            (3, 4, 'wharf_tile_1', 'wharf_spritelayout_water_barge_nw_se'),
            (3, 5, '255', 'wharf_spritelayout_null'),
            (4, 1, '255', 'wharf_spritelayout_null'),
            (4, 2, '255', 'wharf_spritelayout_null'),
            (4, 3, '255', 'wharf_spritelayout_null'),
            (4, 4, '255', 'wharf_spritelayout_null'),
            (4, 5, '255', 'wharf_spritelayout_null'),
            ]
)
