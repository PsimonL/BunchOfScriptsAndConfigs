# Partition adding:
1. After extending the disk resources in VMware vSphere (Bare Metal Type 1 Hypervisor) web console.
2. Host reboot required
3. Display the list of partitions on the specified disk:
```
fdisk -l /dev/sda
```
4. Use the "parted" program to manage disk partitions (/dev/sda is the disk to be edited, pick of your choice):
```
parted /dev/sda
```
5. Display the current state of the partitions:
```
(parted) print
```
6. Resize the partition:
```
(parted) resizepart 2 100GB
(parted) quit
```
7. Inform the LVM (Logical Volume Manager) about the availability of additional space:
```
pvresize /dev/sda2
```
8. *Optional: Add the space to an existing volume group:
```
vgextend host_volume_group /dev/sda2
```
9. Extend the logical volume:
```
lvextend -l +100%FREE /dev/host_volume_group/root
```
10. Enable the additional disk space in the EXT4 filesystem:
```
resize2fs /dev/host_volume_group/root
```
11. *Instead of the above: if the filesystem is XFS:
```
xfs_growfs /
```
12. Check the available disk space:
```
df -h
```

After compliting all above steps should be working fine.