# blockchain-afterwork

Mini-blockchain written with Python 3 and used to explain blockchain concepts.

## Blockchain initialization
```
>>> from blockchain import Blockchain
>>> bc = Blockchain()
>>> bc.add("alpha block")
>>> bc.add("bravo block")
>>> print(bc)

////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 2                                                                              //
//    hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe                      //
//    timestamp: 2018-02-08 12:01:15.414944                                                       //
//    previous_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921       //
//    next_block_hash: None                                                                       //
//    data: bravo block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////
                                                 |
                                                 |
////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 1                                                                              //
//    hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921                      //
//    timestamp: 2018-02-08 12:01:11.800539                                                       //
//    previous_block_hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266       //
//    next_block_hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe           //
//    data: alpha block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////
                                                 |
                                                 |
////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 0                                                                              //
//    hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266                      //
//    timestamp: 2018-02-08 12:01:09.303865                                                       //
//    previous_block_hash: None                                                                   //
//    next_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921           //
//    data: I am the genesis block.                                                               //
////////////////////////////////////////////////////////////////////////////////////////////////////
```

## Demonstrate doubly linked list behaviour
```
>>> bc.navigate_up()
////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 0                                                                              //
//    hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266                      //
//    timestamp: 2018-02-08 12:01:09.303865                                                       //
//    previous_block_hash: None                                                                   //
//    next_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921           //
//    data: I am the genesis block.                                                               //
////////////////////////////////////////////////////////////////////////////////////////////////////

ONE BLOCK UP [PRESS ENTER]

////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 1                                                                              //
//    hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921                      //
//    timestamp: 2018-02-08 12:01:11.800539                                                       //
//    previous_block_hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266       //
//    next_block_hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe           //
//    data: alpha block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////

ONE BLOCK UP [PRESS ENTER]

////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 2                                                                              //
//    hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe                      //
//    timestamp: 2018-02-08 12:01:15.414944                                                       //
//    previous_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921       //
//    next_block_hash: None                                                                       //
//    data: bravo block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////

>>> bc.navigate_down()
////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 2                                                                              //
//    hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe                      //
//    timestamp: 2018-02-08 12:01:15.414944                                                       //
//    previous_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921       //
//    next_block_hash: None                                                                       //
//    data: bravo block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////

ONE BLOCK DOWN [PRESS ENTER]

////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 1                                                                              //
//    hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921                      //
//    timestamp: 2018-02-08 12:01:11.800539                                                       //
//    previous_block_hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266       //
//    next_block_hash: d8b79efb98927dbd318d14138ddec2709010b51aec2674bda221c061970ec2fe           //
//    data: alpha block                                                                           //
////////////////////////////////////////////////////////////////////////////////////////////////////

ONE BLOCK DOWN [PRESS ENTER]

////////////////////////////////////////////////////////////////////////////////////////////////////
//    block_index: 0                                                                              //
//    hash: ac67670df3246909e9f31f284df7f7286200eaa8ab6c327222b257df18420266                      //
//    timestamp: 2018-02-08 12:01:09.303865                                                       //
//    previous_block_hash: None                                                                   //
//    next_block_hash: 1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921           //
//    data: I am the genesis block.                                                               //
////////////////////////////////////////////////////////////////////////////////////////////////////
```

## Demonstrate data immutability
```
>>> block_to_edit = bc.search("1b77a18d24d8ec0e01bc235d5439f6edcd005c3142717863ed935bc33e827921")
>>> block_to_edit.data = "Data has been edited"
>>> print(bc)

/!\ Blockchain is corrupted.
Cant't retrieve blocks before block 2.



```
